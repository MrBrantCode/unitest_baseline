"""
QUESTION:
Replace all vowels with asterisks in a given string. 

The function should be case-insensitive and return the modified string in the same case as the original string. The vowels are 'a', 'e', 'i', 'o', and 'u' (both uppercase and lowercase). The function should have a time complexity of O(n) where n is the length of the input string, use a constant amount of extra space, and handle edge cases such as empty string or a string with no vowels.
"""

def replace_vowels_with_asterisks(s):
    """
    Replaces all vowels with asterisks in a given string.

    The function is case-insensitive and returns the modified string in the same case as the original string.
    
    Parameters:
    s (str): The input string.

    Returns:
    str: The modified string with vowels replaced by asterisks.
    """
    result = ''
    for ch in s:
        if ch.lower() in 'aeiou':
            result += '*' if ch.islower() else '*'
        else:
            result += ch
    return result