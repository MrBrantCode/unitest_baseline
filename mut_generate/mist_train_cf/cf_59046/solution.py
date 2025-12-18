"""
QUESTION:
Implement a function `find_ed_words` that identifies unique words containing the substring "ed" but not at the end, from a given paragraph. The function should count the occurrences of each word, ignoring punctuation and case sensitivity, and return a list of tuples containing the word and its count, sorted in descending order by count.
"""

import re
from collections import Counter

def find_ed_words(paragraph):
    cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph.lower())
    matches = re.findall(r'\b\w*ed\w+\b', cleaned_paragraph)
    word_counts = Counter(matches)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts