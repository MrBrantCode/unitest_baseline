"""
QUESTION:
Create a function `is_rotation(s1, s2)` that checks if `s2` is a rotation of `s1` in O(n) time complexity and O(1) space complexity. Both `s1` and `s2` are strings containing lowercase and uppercase letters, numbers, and special characters, and have the same length.
"""

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_s1 = s1 + s1
    return s2 in s1_s1