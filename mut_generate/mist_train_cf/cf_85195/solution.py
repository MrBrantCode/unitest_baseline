"""
QUESTION:
Create a function called `symbol_frequency` that takes a string `text` as input. The function should be case insensitive, remove all punctuation and spaces, and calculate the frequency of each unique alphabetical symbol and each combination of two adjacent characters in the text. The function should return two dictionaries, one for the frequency of single characters and one for the frequency of double characters.
"""

import re
from collections import defaultdict

def symbol_frequency(text):
    text = text.lower()  # make text case insensitive
    text = re.sub(r'\W+', '', text)  # remove punctuation and spaces

    single_char_frequency = defaultdict(int)
    double_char_frequency = defaultdict(int)

    for i in range(len(text)):
        single_char_frequency[text[i]] += 1
        if i < len(text) - 1:
            double_char_frequency[text[i:i+2]] += 1

    return dict(single_char_frequency), dict(double_char_frequency)