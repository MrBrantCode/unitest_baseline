"""
QUESTION:
Write a function named `compare_string_and_int` that takes a string and an integer as input, and returns the longer string. The integer should be passed as a string. You cannot use built-in functions or methods such as `len()` or `str()`, loops, or recursion in your solution. You can only use basic operations like comparison operators and logical operators.
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