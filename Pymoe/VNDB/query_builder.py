from enum import Enum

class Stype(Enum):
    """
        An Enum for the operation type. Either get or set. Much better than using a string and clearer than using a number.
    """
    get = 1
    set = 2
    
class Datamask(bytearray):
    """
        This is a custom bytearray used by get to map which pieces of information you want back.
        It's also used to determine the minimum amount of flags necessary to get the data.
    """
    def __init__(masks=10):
        super().__init__(masks)
    

class Query:
    """
        Interface to the VNDB Query Builder. 
        Use this to simplify building the queries needed to retrieve data from the VNDB API.
    """
    
    def __init__(self, operation=Stype.get):
        if isinstance(operation, Stype):
            if operation == Stype.get:
                self.bitmask = Datamask(10) # Verify the number of data types
            else:
                # TODO: Write set
        else:
            raise SyntaxError("Operation must be Stype.get or Stype.set.")