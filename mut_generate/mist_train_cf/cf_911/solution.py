"""
QUESTION:
Write a function named `concatenate_string` that takes a string `s` as input and returns a new string that is a concatenation of the original string and a reversed copy of the original string, but only including the alphabetic characters in the reversed copy. The reversed copy should be case-insensitive, treating uppercase and lowercase alphabetic characters as the same. The function should not use any built-in string reversal functions or libraries.
"""

def concatenate_string(s):
    """
    Concatenates the original string with a reversed copy of its alphabetic characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: A new string that is a concatenation of the original string and a reversed copy of its alphabetic characters.
    """
    # Reverse the string without using built-in functions or libraries
    reversed_string = ''
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    
    concatenated_string = ''
    for char in reversed_string:
        if char.isalpha():
            concatenated_string += char.lower()
    
    return s + concatenated_string