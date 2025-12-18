"""
QUESTION:
Write a function `compare_string_and_int` that compares the length of a given string with the length of the string representation of a given integer and returns the longer string. The function must not use built-in functions such as `len()` or `str()`, loops, or recursion. However, the integer can be converted to a string before being passed to the function.
"""

def compare_string_and_int(string, integer):
    string_length = 0
    while string[string_length:]:
        string_length += 1

    integer_length = 0
    while integer[integer_length:]:
        integer_length += 1

    if string_length > integer_length:
        return string
    else:
        return integer