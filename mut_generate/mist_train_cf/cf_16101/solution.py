"""
QUESTION:
Write a function `reverse_string()` that takes a user's input string, removes any leading or trailing white spaces, and returns the reversed string without using any built-in string reversal functions or methods.
"""

def reverse_string(s):
    """
    Reverses a given string after removing leading and trailing white spaces.
    
    Args:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    s = s.strip()  # Remove leading and trailing white spaces
    
    reversed_string = ""  # Initialize an empty string to store the reversed string
    
    for i in range(len(s)-1, -1, -1):  # Iterate through each character in reverse order
        reversed_string += s[i]  # Append each character to the reversed string
    
    return reversed_string  # Return the reversed string