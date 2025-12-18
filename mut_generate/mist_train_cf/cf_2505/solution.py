"""
QUESTION:
Implement a recursive function called `custom_length` that calculates the length of a given string, including spaces and special characters, without using any built-in length functions or methods. The function should handle edge cases such as empty strings, strings with leading or trailing spaces, consecutive spaces, Unicode characters, and non-ASCII characters.
"""

def custom_length(s):
    """
    Calculates the length of a given string, including spaces and special characters,
    without using any built-in length functions or methods.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the input string.
    """

    # Base case: an empty string has length 0
    if s == "":
        return 0
    
    # Recursive case: count the current character and call the function with the remaining substring
    else:
        return 1 + custom_length(s[1:])