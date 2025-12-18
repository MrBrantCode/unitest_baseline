"""
QUESTION:
Write a function `count_distinct_words` that takes a string as input and returns the number of distinct words and a list of the most frequently occurring words in descending order of frequency. The function should ignore any punctuation or special characters and treat uppercase and lowercase letters as distinct words. The time complexity should be O(n) and the space complexity should be O(m), where n is the length of the string and m is the number of distinct words.
"""

import re
from collections import Counter

def count_distinct_words(string):
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    words = cleaned_string.lower().split()
    word_counts = Counter(words)
    distinct_words = word_counts.keys()
    sorted_words = sorted(distinct_words, key=lambda w: word_counts[w], reverse=True)
    return len(distinct_words), sorted_words