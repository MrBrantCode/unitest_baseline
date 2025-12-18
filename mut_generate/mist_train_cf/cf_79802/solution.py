"""
QUESTION:
Write a function `are_isomorphic` that determines whether two given strings are isomorphic without using any predefined or inbuilt function. The function should return `True` if the strings are isomorphic and `False` otherwise. Two strings are isomorphic if the characters in one string can be replaced to get the other string, and this replacement should be one-to-one. The function should only take two parameters: `string1` and `string2`.
"""

def are_isomorphic(string1, string2):
    """
    This function determines whether two given strings are isomorphic.
    
    Args:
        string1 (str): The first string.
        string2 (str): The second string.
    
    Returns:
        bool: True if the strings are isomorphic, False otherwise.
    """
    # initialize two empty dictionaries
    map_char_string1 = {}
    map_char_string2 = {}

    # check if strings have same length
    if len(string1) != len(string2):
        return False

    for char_s1, char_s2 in zip(string1, string2):
        # if char_s1 has not been mapped before
        if char_s1 not in map_char_string1:
            map_char_string1[char_s1] = char_s2
        # if char_s1 is mapped to a different char than char_s2
        elif map_char_string1[char_s1] != char_s2:
            return False

        # if char_s2 has not been mapped before
        if char_s2 not in map_char_string2:
            map_char_string2[char_s2] = char_s1
        # if char_s2 is mapped to a different char than char_s1
        elif map_char_string2[char_s2] != char_s1:
            return False

    return True