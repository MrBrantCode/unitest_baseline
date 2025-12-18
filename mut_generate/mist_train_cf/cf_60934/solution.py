"""
QUESTION:
Write a function `calculate_word_frequency` to calculate the frequency of each distinct word in a given text, maintaining case sensitivity and excluding numbers and special characters. The function should take a string `text` as input and return a dictionary where the keys are the distinct words and the values are their corresponding frequencies.
"""

import re
from collections import Counter

def calculate_word_frequency(text):
    # Find all words in the text
    words = re.findall(r'\b\w+\b', text)

    # Get the frequency for each distinct word
    word_frequency = Counter(words)

    return word_frequency