"""
QUESTION:
Write a function called shift_word that takes a string as input and returns the string with all its letters shifted two characters ahead. The function should handle only lowercase English letters.
"""

def shift_word(word):
    """
    Shifts all the letters in a given word two characters ahead.

    Args:
        word (str): The input word.

    Returns:
        str: The word with all its letters shifted two characters ahead.
    """
    shifted_word = ""
    for char in word:
        if char.isalpha() and char.islower():
            shifted_char = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
            shifted_word += shifted_char
        else:
            shifted_word += char
    return shifted_word