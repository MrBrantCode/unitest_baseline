"""
QUESTION:
Create a function `count_capital_letters` that takes a string as input and returns a dictionary where the keys are the capital letters in the string and the values are the corresponding counts. Use a regular expression to find all the capital letters.
"""

import re

def count_capital_letters(s):
    """
    Returns a dictionary with capital letters as keys and their counts as values.
    
    :param s: Input string
    :return: Dictionary with capital letter counts
    """
    capital_letters = re.findall(r'[A-Z]', s)
    counts = {}
    for letter in capital_letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts