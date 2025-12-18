"""
QUESTION:
Create a function `is_isomorphic(str1, str2)` that checks if two strings `str1` and `str2` are isomorphic. Two strings are isomorphic if the characters in `str1` can be replaced to get `str2`, preserving the order of characters. The function should return `True` if the strings are isomorphic and `False` otherwise.
"""

def is_isomorphic(str1, str2):
    # checking if both strings have same length, otherwise they can't be isomorphic
    if len(str1) != len(str2):
        return False

    # dictionaries to store mappings
    str1_to_str2 = {}
    str2_to_str1 = {}

    for x, y in zip(str1, str2):
        # if x is already mapped, then it should be mapped to the same y, otherwise return False
        if x in str1_to_str2 and str1_to_str2[x] != y:
            return False
        # if y is already being mapped, then it should be mapped from the same x, otherwise return False
        if y in str2_to_str1 and str2_to_str1[y] != x:
            return False
        # store the mapping
        str1_to_str2[x] = y
        str2_to_str1[y] = x

    # all characters are mapped correctly
    return True