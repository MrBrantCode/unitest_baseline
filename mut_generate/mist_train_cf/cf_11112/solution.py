"""
QUESTION:
Write a function called longest_common_prefix that takes a list of strings as input and returns the longest common prefix among all the strings. If there is no common prefix, the function should return an empty string.
"""

def longest_common_prefix(strs):
    """
    This function finds the longest common prefix among all the strings in the input list.
    
    Parameters:
    strs (list): A list of strings.
    
    Returns:
    str: The longest common prefix among all the strings. If there is no common prefix, an empty string is returned.
    """
    if not strs:
        return ""
    
    shortest_str = min(strs, key=len)
    
    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]
    
    return shortest_str