"""
QUESTION:
Create a function `is_isomorphic(str1, str2)` that determines if two input strings `str1` and `str2` are isomorphic. Two strings are isomorphic if the characters in `str1` can be replaced to get `str2` and vice versa, while maintaining a one-to-one correspondence between characters. The function should return `True` if the strings are isomorphic and `False` otherwise. The function must consider all possible character mappings and handle cases where the strings have different lengths.
"""

def is_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1_to_str2_map = {}
    str2_to_str1_map = {}
    
    for ch1, ch2 in zip(str1, str2):
        if ch1 in str1_to_str2_map and str1_to_str2_map[ch1] != ch2:
            return False
        if ch2 in str2_to_str1_map and str2_to_str1_map[ch2] != ch1:
            return False
        str1_to_str2_map[ch1] = ch2
        str2_to_str1_map[ch2] = ch1
    
    return True