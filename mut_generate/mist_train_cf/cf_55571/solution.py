"""
QUESTION:
Design a function `is_rotation(str1, str2)` that checks if one string is a rotation of the other. The function should return `True` if `str2` is a rotation of `str1` and `False` otherwise. The function should only consider exact rotations, i.e., no characters are added or removed. Assume the input strings only contain lowercase letters. The function should be case sensitive and not consider uppercase letters. The length of the strings can be up to several thousand characters.
"""

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        concat = str1 + str1
        if str2 in concat:
            return True
        else:
            return False