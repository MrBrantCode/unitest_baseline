"""
QUESTION:
Construct a function named `word_count` that takes a string as input and returns a dictionary with words and their corresponding counts of occurrences. The function should ignore case sensitivity and punctuation marks, and only include words with a count greater than 1 in the output dictionary.
"""

import re
from collections import defaultdict

def word_count(input_string):
    # Create a defaultdict with default value 0
    word_counts = defaultdict(int)
    
    # Remove punctuation marks and convert the string to lowercase
    cleaned_string = re.sub(r'[^\w\s]', '', input_string.lower())
    
    # Split the cleaned string into words
    words = cleaned_string.split()
    
    # Count the occurrences of each word
    for word in words:
        word_counts[word] += 1
    
    # Filter out words with count less than or equal to 1
    word_counts = {word: count for word, count in word_counts.items() if count > 1}
    
    return word_counts