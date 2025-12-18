"""
QUESTION:
Write a function called `validate_string` that takes two parameters: `string` and `length`. The function should return `True` if the length of `string` is equal to `length` and `string` contains only lowercase alphabets, and `False` otherwise.
"""

def validate_string(string, length):
    return len(string) == length and string.islower()