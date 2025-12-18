"""
QUESTION:
Create a function `create_dictionary(keys, values)` that takes two lists as input and returns a dictionary where the elements of the first list are the keys and the elements of the second list are the values. The function should raise a `ListLengthMismatchException` if the lengths of the two lists are not equal, and a `ValueTypeMismatchException` if any value in the second list is not of string data type. All keys in the resulting dictionary should be unique and of string data type.
"""

class ListLengthMismatchException(Exception):
    pass

class ValueTypeMismatchException(Exception):
    pass

def create_dictionary(keys, values):
    if len(keys) != len(values):
        raise ListLengthMismatchException("Length of keys and values lists must be equal")
    
    dictionary = {}
    for i in range(len(keys)):
        if not isinstance(keys[i], str):
            keys[i] = str(keys[i])
        if not isinstance(values[i], str):
            raise ValueTypeMismatchException("Values must be of string data type")
        dictionary[keys[i]] = values[i]
    
    return dictionary