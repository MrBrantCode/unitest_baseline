"""
QUESTION:
Write a function called `count_letters` that takes a string as input and returns a dictionary with the total count of each letter of the alphabet it contains. The dictionary should be sorted in decreasing order of frequency, and for equal frequencies, it should be sorted in lexicographical order. The function should handle case-insensitivity (recognizing 'a' and 'A' as the same letter) and ignore special characters and numbers.
"""

from collections import Counter
import re

def count_letters(text):
    text = re.sub(r'[^A-Za-z]', '', text)  # Remove non-alphabet characters
    counter = Counter(text.lower())  # Count frequency of each letter
    return {k: v for k, v in sorted(counter.items(), key=lambda item: (-item[1], ord(item[0])))}