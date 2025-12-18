"""
QUESTION:
Create a function named `count_words` that takes a string `text` as input and returns a dictionary containing all the unique words in the text and their respective frequencies. The function should ignore case sensitivity and special characters, such as punctuation marks. The solution should be optimized for space complexity.
"""

import re
from collections import defaultdict

def count_words(text):
    word_counts = defaultdict(int)
    words = re.findall(r'\w+', text.lower())
    
    for word in words:
        word_counts[word] += 1
    
    return dict(word_counts)