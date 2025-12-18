"""
QUESTION:
Create a function named `remove_vowels_and_special_chars` that takes a string `text` as input and returns a string containing only alphanumeric characters with all vowels removed. The function should work for strings of any length, including empty strings, and should handle both lowercase and uppercase vowels. The output string should be a concatenation of all alphanumeric characters that are not vowels, in the order they appear in the input string.
"""

def remove_vowels_and_special_chars(text):
    """
    Remove vowels and special characters from the given string.

    Parameters:
        text (str): Input string of any length

    Returns:
        str: Processed string with vowels and special characters removed

    """
    vowels = 'aeiouAEIOU'
    result = ''

    for char in text:
        if char.isalnum() and char not in vowels:
            result += char
    
    return result