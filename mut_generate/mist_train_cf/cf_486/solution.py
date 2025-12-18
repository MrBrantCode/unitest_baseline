"""
QUESTION:
Create a function called `string_length` that takes a string `s` as input and returns the length of the string. The function should not use any built-in string length functions or methods, numerical or mathematical operations, or recursion. It should be able to handle cases where the input is not a string or is `None`.
"""

def string_length(s):
    try:
        count = 0
        for _ in s:
            count += 1
        return count
    except TypeError:
        return 0