"""
QUESTION:
Write a function `is_rotation(str1, str2)` to determine if `str2` is a rotation of `str1`. The function should return `True` if `str1` and `str2` are rotations of each other and `False` otherwise. The function must have a time complexity of O(n), where n is the length of the strings, and it must not use any extra space.
"""

def is_rotation(str1, str2):
    # Check if both strings have the same length
    if len(str1) != len(str2):
        return False
    
    # Concatenate str1 with itself
    str1 += str1
    
    # Check if str2 is a substring of str1
    if str2 in str1:
        return True
    
    return False