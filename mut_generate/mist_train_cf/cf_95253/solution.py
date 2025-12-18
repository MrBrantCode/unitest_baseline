"""
QUESTION:
Write a function named `is_rotation` that checks if one string is a rotation of another. The function should take two strings of equal length as input and return `True` if the strings are rotations of each other and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the strings, and should not use any extra space.
"""

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    # Concatenate s1 with itself
    concat_str = s1 + s1
    
    # Check if s2 is a substring of concat_str
    return s2 in concat_str