"""
QUESTION:
Write a function `are_isomorphic(str1, str2)` that checks if two strings of equal length are isomorphic to each other. A string is isomorphic to another if there exists a one-to-one mapping for every letter of the first string to every letter of the second string. The function should return `True` if the strings are isomorphic and `False` otherwise. Assume that the input strings only contain lowercase English letters.
"""

def are_isomorphic(str1, str2):
    mapping_str1_str2 = {}
    mapping_str2_str1 = {}

    for char1, char2 in zip(str1, str2):
        if (char1 in mapping_str1_str2 and mapping_str1_str2[char1] != char2) or \
           (char2 in mapping_str2_str1 and mapping_str2_str1[char2] != char1):
            return False

        else:
            mapping_str1_str2[char1] = char2
            mapping_str2_str1[char2] = char1

    return True