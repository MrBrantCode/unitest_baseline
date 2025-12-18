"""
QUESTION:
Write a function `replace_vowels` that takes two parameters: a string `string` with at least three words and a replacement character `replacement_char`. The function should replace all vowels in the string with the replacement character and return the modified string along with the total count of vowel replacements. The string may contain punctuation and other non-alphabetic characters, which should be left unchanged.
"""

def replace_vowels(string, replacement_char):
    """
    Replace all vowels in a string with a replacement character.

    Args:
        string (str): The input string.
        replacement_char (str): The character to replace vowels with.

    Returns:
        tuple: A tuple containing the modified string and the total count of vowel replacements.
    """
    vowels = "aeiou"
    count = 0
    new_string = ""

    for char in string:
        if char.lower() in vowels:
            new_string += replacement_char
            count += 1
        else:
            new_string += char

    return new_string, count