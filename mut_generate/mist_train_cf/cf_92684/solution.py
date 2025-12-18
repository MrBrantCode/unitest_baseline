"""
QUESTION:
Write a function `get_top_words` that takes a string as input, removes any punctuation and special characters, filters out words containing numbers, and returns the top 10 most frequent words in the string, excluding any words with numbers or special characters, along with their frequency.
"""

import re
from collections import Counter

def get_top_words(string):
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    words = cleaned_string.split()
    words = [word for word in words if word.isalpha()]
    word_count = Counter(words)
    top_words = word_count.most_common(10)
    return top_words