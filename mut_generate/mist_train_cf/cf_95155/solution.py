"""
QUESTION:
Write a function called `is_rotation` that takes two strings as input and returns `True` if the strings are rotations of each other and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the strings. The strings are guaranteed to contain only lowercase alphabets. You are not allowed to use any built-in string rotation or string manipulation functions in your algorithm.
"""

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    concatenated = str1 + str1
    return str2 in concatenated