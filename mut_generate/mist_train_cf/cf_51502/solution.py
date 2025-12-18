"""
QUESTION:
Create a function `find_most_common_word` that takes a string of text as input and returns the most frequently occurring word and its frequency. The function should be case insensitive and consider only word characters (letters and numbers) as valid parts of a word. If the input string is empty, the function should return None and 0.
"""

from collections import Counter
import re

def find_most_common_word(text):
    # split text into words, case insensitive
    words = re.findall(r'\b\w+\b', text.lower())
    # count frequency of each word
    word_counts = Counter(words)
    # get the most common word and its count
    most_common_word = word_counts.most_common(1)
    if most_common_word:
        word, count = most_common_word[0]
        return word, count
    else:
        return None, 0