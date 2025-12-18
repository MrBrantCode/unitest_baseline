"""
QUESTION:
Write a function `is_isomorphic(str1, str2)` that takes two strings as input and returns `True` if they are isomorphic, meaning each character in `str1` can be mapped to exactly one character in `str2` and vice versa, and `False` otherwise.
"""

def is_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_map = {}
    str2_map = {}

    for char1, char2 in zip(str1, str2):
        if char1 not in str1_map and char2 not in str2_map:
            str1_map[char1] = char2
            str2_map[char2] = char1
        elif str1_map.get(char1) != char2 or str2_map.get(char2) != char1:
            return False
    return True