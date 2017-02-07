from .objects import *

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
