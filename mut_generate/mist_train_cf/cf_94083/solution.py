"""
QUESTION:
Write a function `compare_string_int` that takes a string and an integer as input and returns the longer string representation of the two. The string and integer lengths are compared based on the number of characters and digits respectively. The function must not use built-in functions or methods such as `len()` or `str()`, and must not use any loops or recursion.
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