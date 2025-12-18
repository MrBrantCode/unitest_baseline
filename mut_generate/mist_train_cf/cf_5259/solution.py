"""
QUESTION:
Create a function `pattern_match` that takes an array of strings `arr` and a value `x` as input, and returns `True` if `x` matches the pattern of any string in `arr`, and `False` otherwise. The pattern for each string in `arr` is defined as: the string starts with a lowercase letter, followed by any number of uppercase letters, and ends with a digit.
"""

def pattern_match(arr, x):
    for string in arr:
        if string[0].islower() and string[1:-1].isupper() and string[-1].isdigit():
            if x == string:
                return True
    return False