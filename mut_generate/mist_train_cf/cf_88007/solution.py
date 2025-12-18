"""
QUESTION:
Write a function named `is_rotation` that determines if two input strings are rotations of each other. The function should return True if the strings are rotations of each other, and False otherwise. The function must handle strings containing only lowercase alphabets, have a time complexity of O(n), where n is the length of the strings, and a space complexity of O(1), meaning it should not use any additional data structures or arrays. The function should not use any built-in string rotation or string manipulation functions.
"""

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    concat_str = str1 + str1
    return str2 in concat_str