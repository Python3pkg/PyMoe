from Enum import IntEnum


class Operation(IntEnum):
    """
        An IntEnum for the operation type. Either get or set. Much better than using a string and clearer than using a number.
    """
    get = 1
    set = 2

class Datatype(IntEnum):
    """
        An IntEnum for declaring what data you're requesting from the API.
    """
    vn = 0
    release = 1
    producer = 2
    character = 3
    user = 4
    votelist = 5
    vnlist = 6
    wishlist = 7

class Vn(IntEnum):
    """
        An IntEnum that associates each bit in the Datamask to a data item for VN results.
    """
    title = 0
    original = 1
    released = 2
    languages = 3
    orig_lang = 4
    platforms = 5
    aliases = 6
    length = 7
    description = 8
    links = 9
    image = 10
    image_nsfw = 11
    anime = 12
    relations = 13
    tags = 14
    popularity = 15
    rating = 16
    votecount = 17
    screens = 18

class Release(IntEnum):
    """
        An IntEnum that associates each bit in the Datamask to a data item for Release results.
    """
    title = 0
    original = 1
    released = 2
    type = 3
    patch = 4
    freeware = 5
    doujin = 6
    languages = 7
    website = 8
    notes = 9
    minage = 10
    gtin = 11
    catalog = 12
    platforms = 13
    media = 14
    vn = 15
    producers = 16

class Producer(IntEnum):
    """
        An IntEnum that associates each bit in the Datamask to a data item for VN results.
    """
    name = 0
    original = 1
    type = 2
    language = 3
    links = 4
    aliases = 5
    description = 6
    relations = 7

class Character(IntEnum):
    """
        An IntEnum that associates each bit in the Datamask to a data item for VN results.
    """
    name = 0
    original = 1
    gender = 2
    bloodt = 3
    birthday = 4
    aliases = 5
    description = 6
    image = 7
    bust = 8
    waist = 9
    hip = 10
    height = 11
    weight = 12
    traits = 13
    vns = 14

class Datamask(bytearray):
    """
        This is a custom bytearray used by get to map which pieces of information you want back.
        It's also used to determine the minimum amount of flags necessary to get the data.
    """
    def __init__(self, masks=10, type):
        super().__init__(masks)
        self.mask_type = type

    def set_mask(self, thing):
        if isinstance(thing, IntEnum):
            if self.mask_type == Datatype.vn and not isinstance(thing, Vn):
                raise SyntaxError("You're attempting to modify a VN's datamask with the wrong mask type. Please use a Vn mask.")
            else:
                self.flip_bit(thing)
        else:
            raise SyntaxError("This expects an IntEnum. Please use one of the IntEnums from the library.")

    def flip_bit(self, bit):
        self.__setitem__(bit, 0) if self.__getitem__(bit) else self.__setitem__(bit, 1)

    def calculate_flag_mask(self):
        flags = []
        if self.mask_type == Datatype.vn:
            flags.append("basic") if any([self.__getitem__(x) for x in range(6)])
            flags.append("details") if any([self.__getitem__(x) for x in range(6,12)])
            flags.append("anime") if self.__getitem__(12)
            flags.append("relations") if self.__getitem__(13)
            flags.append("tags") if self.__getitem__(14)
            flags.append("stats") if any([self.__getitem__(x) for x in range(15, 18)])
            flags.append("screens") if self.__getitem__(18)
        return flags
