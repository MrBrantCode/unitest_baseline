"""
QUESTION:
Write a function named `count_capital_letters` that takes a string as input, finds all the capital letters in the string, and returns a dictionary where the keys are the capital letters and the values are the corresponding counts. The function should use regular expressions to find the capital letters.
"""

import re

def count_capital_letters(text):
    """
    This function takes a string as input, finds all the capital letters 
    in the string, and returns a dictionary where the keys are the 
    capital letters and the values are the corresponding counts.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with capital letters as keys and their counts as values.
    """

    # Find all capital letters using a regular expression
    capital_letters = re.findall(r'[A-Z]', text)

    # Count the frequency of each capital letter
    counts = {}
    for letter in capital_letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts