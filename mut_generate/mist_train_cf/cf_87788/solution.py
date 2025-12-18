"""
QUESTION:
Create a function called `word_count` that takes a string as input and returns a dictionary where the keys are the words in the string and the values are the number of occurrences of each word. The function should be case-insensitive and ignore punctuation, but it should count words with special characters (such as accented characters) and words with apostrophes as separate words. The function should be able to handle multi-line input strings and very large input strings efficiently.
"""

import re
from collections import defaultdict

def word_count(string):
    word_dict = defaultdict(int)
    lines = string.split('\n')
    
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            word_dict[word] += 1
    
    return dict(word_dict)