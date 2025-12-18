"""
QUESTION:
Create a function `are_rotations(str1, str2)` that determines if two strings are rotations of each other. The function should return `True` if the strings are rotations of each other and `False` otherwise. The input strings contain only lowercase alphabets and have the same length. The function should have a time complexity of O(n), where n is the length of the strings.
"""

def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    return str2 in str1 + str1