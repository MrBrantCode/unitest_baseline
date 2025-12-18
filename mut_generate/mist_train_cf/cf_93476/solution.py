"""
QUESTION:
Write a function `check_strings(arr)` that takes a sequence of strings `arr` as input and returns `True` if all strings in the sequence are unique and contain only lowercase alphabets, and `False` otherwise.
"""

def entrance(arr):
    unique_strings = set()
    for string in arr:
        if not string.islower():
            return False
        if string in unique_strings:
            return False
        unique_strings.add(string)
    return True