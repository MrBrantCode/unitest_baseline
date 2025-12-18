"""
QUESTION:
Write a function `check_strings(arr)` that takes an array of strings `arr` as input and returns `True` if all strings in `arr` contain at least two digits and two uppercase letters, and `False` otherwise.
"""

def check_strings(arr):
    def has_required_characters(string):
        digits = sum(1 for char in string if char.isdigit())
        uppercase = sum(1 for char in string if char.isupper())
        return digits >= 2 and uppercase >= 2

    return all(has_required_characters(string) for string in arr)