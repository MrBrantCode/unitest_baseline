"""
QUESTION:
Write a function `are_isomorphic(string1, string2)` that checks if two given strings `string1` and `string2` are isomorphic to each other. Two strings are isomorphic if the characters in `string1` can be replaced with any other characters to get `string2` without mapping two characters from `string1` to the same character in `string2`. Return `True` if the strings are isomorphic and `False` otherwise.
"""

def are_isomorphic(string1, string2):
    if len(string1) != len(string2):
        return False

    mapping_str1 = {}
    mapping_str2 = {}

    for char1, char2 in zip(string1, string2):
        if (char1 in mapping_str1 and mapping_str1[char1] != char2) or (char2 in mapping_str2 and mapping_str2[char2] != char1):
            return False
        mapping_str1[char1] = char2
        mapping_str2[char2] = char1

    return True