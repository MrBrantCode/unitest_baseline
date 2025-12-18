"""
QUESTION:
Design a function `find_palindrome_frequency` that takes a string `script` as input and returns a dictionary of palindromic words and their frequencies. The function should consider a word as palindromic if it reads the same forwards and backwards, regardless of case, and ignore non-alphabetic characters. The function should return a dictionary where the keys are the palindromic words in lowercase and the values are their corresponding frequencies.
"""

import re
from collections import defaultdict

def find_palindrome_frequency(script):
    script = script.lower()     # Convert all to lower case
    script = re.sub(r'\W+', ' ', script)  # Remove all non-alphabetic characters
    words = script.split()

    # Create a dictionary to store word frequencies
    word_frequencies = defaultdict(int)

    for word in words:
        # Check if the word is a palindrome
        if word == word[::-1]:
            word_frequencies[word] += 1

    return word_frequencies