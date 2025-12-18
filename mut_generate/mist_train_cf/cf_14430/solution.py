"""
QUESTION:
Create a function `replace_vowels` that takes a string `text` and a character `char` as input. Replace all vowels (except 'y') in the text with the given character and return the updated text along with the count of replaced vowels. The function should be case-insensitive when checking for vowels.
"""

def replace_vowels(text, char):
    """
    Replace all vowels (except 'y') in the text with the given character and return the updated text along with the count of replaced vowels.
    
    Args:
    text (str): The input string.
    char (str): The character to replace vowels with.
    
    Returns:
    tuple: A tuple containing the updated text and the count of replaced vowels.
    """
    
    count = 0
    for letter in text:
        if letter.lower() in "aeiou":
            count += 1
            text = text.replace(letter, char)
    
    return text, count