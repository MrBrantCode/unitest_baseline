"""
QUESTION:
Write a function `remove_vowels` that takes a string as input, removes all vowels from the string, and returns the modified string along with its length. The function should be case-insensitive when identifying vowels.
"""

def remove_vowels(s):
    """
    This function removes all vowels from a given string and returns the modified string along with its length.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    tuple: A tuple containing the modified string and its length.
    """
    vowels = 'aeiouAEIOU'
    modified_string = ''.join([char for char in s if char not in vowels])
    return modified_string, len(modified_string)