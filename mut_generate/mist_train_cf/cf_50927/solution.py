"""
QUESTION:
Create a function `validate_string(s)` that takes a string `s` as input and returns the integer equivalent if the string can be successfully converted to a whole number, otherwise returns an error message. The function should handle cases where the input string is null, empty, contains whitespace, or is a non-integer string. The function should not consider floating point numbers as valid integers.
"""

def validate_string(s):
    if s is None or len(s.strip()) == 0:
        return "Error: Input is null or empty"
    elif s.strip().isdigit():
        return int(s)
    else:
        return "Error: Cannot convert to a whole number"