"""
QUESTION:
Write a function `findFirstNonDuplicateChar(s)` to find the first non-duplicate character in a given string `s`. The function should return the first character that appears only once in the string. If no such character exists, it may return an empty string or handle it as desired. The input string `s` contains only lowercase letters.
"""

def findFirstNonDuplicateChar(s):
    """
    This function finds the first non-duplicate character in a given string.
    
    Parameters:
    s (str): The input string containing only lowercase letters.
    
    Returns:
    str: The first character that appears only once in the string. If no such character exists, an empty string is returned.
    """
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return ""