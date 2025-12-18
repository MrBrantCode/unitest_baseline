"""
QUESTION:
Create a Python function named `create_dictionary(keys, values)` that takes two lists as input and returns a dictionary. The function should ensure all keys in the resulting dictionary are unique and of string data type, and all values are of string data type. If the lengths of the two lists are not equal, the function should raise a custom `ListLengthMismatchException`. If any of the values in the second list are not of string data type, the function should raise a custom `ValueTypeMismatchException`.
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