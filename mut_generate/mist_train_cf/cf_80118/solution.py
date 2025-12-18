"""
QUESTION:
Create a function `is_isomorphic(str1, str2)` that determines if two input strings are isomorphic without using external libraries, recursive methods, or built-in functions. Two strings are isomorphic if the sequence of unique character occurrences in both strings is the same. The function should return a boolean value indicating whether the strings are isomorphic or not.
"""

def is_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    map_str1 = [0] * 256
    map_str2 = [0] * 256

    for i in range(len(str1)):
        if map_str1[ord(str1[i])] != map_str2[ord(str2[i])]:
            return False
        map_str1[ord(str1[i])] = i+1
        map_str2[ord(str2[i])] = i+1

    return True