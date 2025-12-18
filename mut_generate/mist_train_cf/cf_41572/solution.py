"""
QUESTION:
Create a function `count_unique_words(disclaimer)` that takes a multi-line string `disclaimer` as input and returns the count of unique words in alphabetical order, ignoring case sensitivity and considering words with different punctuation as the same word. The function should output the unique words along with their respective counts.
"""

import re
from collections import defaultdict

def count_unique_words(disclaimer):
    disclaimer = disclaimer.lower()  
    words = re.findall(r'\b\w+\b', disclaimer)  
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1  
    return dict(sorted(word_count.items()))