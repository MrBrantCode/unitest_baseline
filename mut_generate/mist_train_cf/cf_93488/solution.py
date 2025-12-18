"""
QUESTION:
Create a function named `letter_frequency` that takes a string `text` as input and returns a dictionary with the frequency of each letter in the text. The function should ignore non-alphabet characters and be case-insensitive. The output should be sorted in descending order of frequency.
"""

from collections import Counter
import re

def letter_frequency(text):
    cleaned_text = re.sub(r'[^a-zA-Z]', '', text.lower())
    letter_count = Counter(cleaned_text)
    sorted_letter_count = dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))
    return sorted_letter_count