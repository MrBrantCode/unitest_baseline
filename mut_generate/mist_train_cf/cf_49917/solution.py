"""
QUESTION:
Create a function called `handle_dict_keys` that takes an input and returns a dictionary where each key is the data type of the original input's keys and each value is a list of keys of that type from the original input. The function should raise a custom exception called `InvalidDataTypeException` if the input is not a dictionary. The exception should have a default message "Input is not a dictionary".
"""

class InvalidDataTypeException(Exception):
    def __init__(self, message="Input is not a dictionary"):
        super().__init__(message)

def handle_dict_keys(d):
    if not isinstance(d, dict):
        raise InvalidDataTypeException()
    result = {}
    for key in d.keys():
        key_type = type(key)
        if key_type not in result:
            result[key_type] = [key]
        else:
            result[key_type].append(key)
    return result