"""
QUESTION:
Implement a function named `reverse_string` that takes a string of alphanumeric characters, removes all non-alphanumeric characters (including whitespace, punctuation, and special characters), and reverses the remaining characters in place using recursion. The function should handle both uppercase and lowercase characters and return the reversed string.
"""

def reverse_string(s):
    """
    Reverses a string of alphanumeric characters by removing non-alphanumeric characters 
    and reversing the remaining characters in place using recursion.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """
    
    # Base case: if the string is empty or only contains one character, return the string
    if len(s) <= 1:
        return s
    
    # Remove whitespace characters and punctuation marks
    s = ''.join(char for char in s if char.isalnum())
    
    # Reverse the string by swapping the first and last characters and recursively calling the function on the remaining substring
    return reverse_string(s[1:]) + s[0]