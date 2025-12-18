"""
QUESTION:
Write a function `check_sequence(arr)` that takes a sequence of strings as input and returns `True` if all strings in the sequence are unique, contain only lowercase alphabets, and have a length between 3 and 10 characters (inclusive). Otherwise, it should return `False`.
"""

def check_sequence(arr):
    # Check for uniqueness
    if len(set(arr)) != len(arr):
        return False

    # Check for lowercase alphabets and length between 3 and 10 characters
    for string in arr:
        if not string.islower() or not (3 <= len(string) <= 10):
            return False

    return True