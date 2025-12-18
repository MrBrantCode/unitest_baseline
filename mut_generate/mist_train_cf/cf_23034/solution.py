"""
QUESTION:
Create a function `convert_string` that takes a string as input, converts it to lowercase, removes all vowels, and returns the resulting string in reverse order. The vowels to be removed are 'a', 'e', 'i', 'o', and 'u'.
"""

def convert_string(s):
    """
    This function takes a string as input, converts it to lowercase, 
    removes all vowels, and returns the resulting string in reverse order.

    Parameters:
    s (str): The input string.

    Returns:
    str: The resulting string after conversion, vowel removal, and reversal.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([char for char in s.lower() if char not in vowels])[::-1]