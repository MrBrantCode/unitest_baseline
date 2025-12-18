"""
QUESTION:
Create a function named `word_count` that takes a string of multiple sentences as input. The function should return a dictionary where the keys are the unique words from the input string and the values are their respective counts. The function should ignore case sensitivity and punctuation marks, and only include words with a count greater than 1 in the output dictionary.
"""

import re
from collections import defaultdict

def word_count(input_string):
    word_counts = defaultdict(int)
    
    cleaned_string = re.sub(r'[^\w\s]', '', input_string.lower())
    
    words = cleaned_string.split()
    
    for word in words:
        word_counts[word] += 1
    
    word_counts = {word: count for word, count in word_counts.items() if count > 1}
    
    return word_counts