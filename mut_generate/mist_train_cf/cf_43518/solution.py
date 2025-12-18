"""
QUESTION:
Design a function named `find_palindromes` that takes a string of text as input. The function should split the input text into words, identify the distinct palindromic sequences (case-insensitive and without considering punctuation as part of palindromes), and return the count and the set of distinct palindromes.
"""

import re

def find_palindromes(text):
    """
    This function takes a string of text as input, identifies the distinct palindromic sequences 
    (case-insensitive and without considering punctuation as part of palindromes), 
    and returns the count and the set of distinct palindromes.

    Args:
        text (str): The input text.

    Returns:
        tuple: A tuple containing the count and the set of distinct palindromes.
    """

    # Split the input text into words and convert to lower case
    words = re.findall(r'\b\w+\b', text.lower())

    # Use set to automatically handle duplicates
    palindromes = set()

    # Iterate over each word and check if it is a palindrome
    for word in words:
        if word == word[::-1]:   # Check if the word is the same when reversed
            palindromes.add(word)

    # Return the count and the set of distinct palindromes
    return len(palindromes), palindromes