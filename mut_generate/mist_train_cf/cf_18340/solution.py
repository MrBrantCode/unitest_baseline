"""
QUESTION:
Create a function `is_rotation` that takes two strings `str1` and `str2` as input, both containing only lowercase alphabets, and returns `True` if `str1` and `str2` are rotations of each other, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the strings, and should not use any built-in string rotation or string manipulation functions.
"""

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    concatenated = str1 + str1
    if str2 in concatenated:
        return True
    else:
        return False