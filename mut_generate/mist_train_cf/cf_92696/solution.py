"""
QUESTION:
Create a function `sort_string` that takes a string of multiple words as input. The function should remove any duplicate words, ignore any words containing numbers or special characters, sort the remaining words alphabetically by their length in descending order, and return the sorted words as a string.
"""

import re

def sort_string(string):
    # Split the string into individual words
    words = string.split()

    # Remove duplicate words
    words = list(set(words))

    # Remove words containing numbers or special characters
    words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]

    # Sort the words based on their length in descending order
    words.sort(key=len, reverse=True)

    # Return the sorted words as a string
    return ' '.join(words)