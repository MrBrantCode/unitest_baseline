"""
QUESTION:
Implement a function named `reverse_strings` that takes two strings as input. The function should ignore any leading or trailing whitespace in the input strings, and return the reversed strings concatenated together with a hyphen and a space in between. If the length of the strings are not equal, return an empty string. The function should be case-sensitive, handle strings containing special characters and non-alphabetic characters, and have a time complexity of O(n), where n is the length of the longer input string.
"""

def reverse_strings(s1, s2):
    """
    This function takes two strings as input, reverses them, and returns the 
    reversed strings concatenated together with a hyphen and a space in between.
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
    
    Returns:
        str: The reversed strings concatenated together with a hyphen and a space 
             in between if the input strings are of equal length. Otherwise, an 
             empty string is returned.
    """
    s1 = s1.strip()
    s2 = s2.strip()
    
    if len(s1) != len(s2):
        return ""
    
    return s2[::-1] + " - " + s1[::-1]