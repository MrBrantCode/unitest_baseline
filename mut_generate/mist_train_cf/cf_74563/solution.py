"""
QUESTION:
Create a function named `special_func` that takes one input parameter `input_value`. The function should return the square of `input_value` if it's a number (int or float), convert it to uppercase if it's a string, return its inverse value if it's a boolean, and return a message specifying the datatype if it's any other datatype.
"""

def special_func(input_value):
    if isinstance(input_value, int) or isinstance(input_value, float):
        return input_value**2
    elif isinstance(input_value, str):
        return input_value.upper()
    elif isinstance(input_value, bool):
        return not input_value
    else:
        return "Unhandled datatype: " + str(type(input_value))