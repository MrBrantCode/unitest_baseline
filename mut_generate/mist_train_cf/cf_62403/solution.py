"""
QUESTION:
Create a function named `replace_vowels_with_star` that takes a string `text` as input. Replace all vowels (both lowercase and uppercase) in `text` with an asterisk (*) and return the modified string. The function should handle any type of string input.
"""

def replace_vowels_with_star(text):
    """
    Replace all vowels (both lowercase and uppercase) in the input string with an asterisk (*).

    Args:
        text (str): The input string.

    Returns:
        str: The modified string with vowels replaced.
    """
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        text = text.replace(vowel, "*")
    return text