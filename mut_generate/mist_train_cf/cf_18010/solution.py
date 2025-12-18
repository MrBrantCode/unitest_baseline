"""
QUESTION:
Write a function `longest_common_suffix` that takes a list of strings as input and returns the longest common suffix among all the strings. If there is no common suffix, return an empty string. The function should work for any number of input strings.
"""

def longest_common_suffix(strings):
    """
    This function takes a list of strings as input and returns the longest common suffix among all the strings.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        str: The longest common suffix among all the strings. If there is no common suffix, returns an empty string.
    """
    if not strings:
        return ""

    min_len = min(len(s) for s in strings)
    for i in range(min_len, -1, -1):
        suffix = strings[0][-i:]
        if all(s.endswith(suffix) for s in strings):
            return suffix

    return ""