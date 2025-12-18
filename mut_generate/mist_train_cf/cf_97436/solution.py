"""
QUESTION:
Write a function called `reverse_words` that takes a string as input, splits it into words, and returns a new string with the words in reverse order. The function should ignore any leading or trailing spaces in the input string, handle cases where there are multiple spaces between words, and treat punctuation marks and special characters within words as part of those words.
"""

import re

def reverse_words(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Split the string into words
    words = re.split(r'\s+', string)

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string