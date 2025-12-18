"""
QUESTION:
Create a function called `remove_vowels_and_reverse` that takes a string as input and returns a new string with all vowels removed and the remaining characters reversed.
"""

def remove_vowels_and_reverse(s):
    """
    This function takes a string as input, removes all vowels, and reverses the remaining characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    str: A new string with all vowels removed and the remaining characters reversed.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])[::-1]