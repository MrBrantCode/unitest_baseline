"""
QUESTION:
Create a function `is_rotation(string1, string2)` that checks if `string1` and `string2` are rotations of each other in either direction. The function should return `True` if `string1` and `string2` are rotations of each other, and `False` otherwise. The function must handle cases where `string1` and `string2` have different lengths, in which case they cannot be rotations of each other.
"""

def is_rotation(string1, string2):
    if len(string1) != len(string2):
        return False

    temp = string1 + string1
    return string2 in temp