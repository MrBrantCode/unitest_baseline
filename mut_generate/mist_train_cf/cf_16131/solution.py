"""
QUESTION:
Write a function `compare_string_int(string, num)` that takes a string and an integer as input and returns the longer one as a string. You cannot use built-in functions or methods, loops, or recursion in your solution.
"""

def compare_string_int(string, num):
    string_length = 0
    while string[string_length: string_length + 1] != "":
        string_length += 1

    num_length = 0
    while num // (10 ** num_length) != 0:
        num_length += 1

    if string_length > num_length:
        return string
    else:
        return str(num)