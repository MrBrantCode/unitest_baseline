"""
QUESTION:
Implement a function `reverse_words` that takes a string as a parameter and returns a modified string with the words reversed, while preserving the original order of non-space characters within each word. The function should remove any leading or trailing whitespace from the input string, convert multiple spaces between words into a single space, and handle special characters, numbers, and non-Latin characters in the string.
"""

import re

def reverse_words(string):
    # Remove leading and trailing whitespace
    string = string.strip()

    # Replace multiple spaces with a single space
    string = re.sub('\s+', ' ', string)

    # Split the string into a list of words
    words = string.split()

    # Reverse the order of words
    words.reverse()

    # Join the reversed words back into a string
    reversed_string = ' '.join(words)

    return reversed_string