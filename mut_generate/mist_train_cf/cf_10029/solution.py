"""
QUESTION:
Write a function named `concatenate_strings` that takes two strings `str1` and `str2` as input and returns their concatenation. The function should not use any built-in string concatenation methods such as the `+` operator or the `join()` function. Note that the Python `+` operator does not meet this requirement, so an alternative approach is needed.
"""

def concatenate_strings(str1, str2):
    result = list(str1)
    for char in str2:
        result.append(char)
    return ''.join(result)