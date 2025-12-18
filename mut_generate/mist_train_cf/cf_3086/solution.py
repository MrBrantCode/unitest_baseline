"""
QUESTION:
Create a function named `word_count` that takes a string of words as input and returns a dictionary with the words as keys and the number of occurrences of each word as values. The function should ignore punctuation, be case-insensitive, handle special characters and words with apostrophes properly, and efficiently handle large input strings with millions of words. The input string can contain multiple lines separated by newline characters.
"""

import re
from collections import defaultdict

def word_count(string):
    word_dict = defaultdict(int)
    lines = string.split('\n')
    
    for line in lines:
        words = re.findall(r"\b[\w']+\b", line.lower())
        for word in words:
            word_dict[word] += 1
    
    return dict(word_dict)