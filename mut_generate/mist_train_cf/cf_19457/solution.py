"""
QUESTION:
Create a function named `word_count` that takes a string of maximum length 1000 characters as input and returns a dictionary where each key is a unique word and its corresponding value is the number of times it appears in the string. The function should ignore punctuation marks, treat uppercase and lowercase letters as the same, and handle cases where words are separated by multiple spaces or tabs. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import re
from collections import Counter

def word_count(s):
    """
    Returns a dictionary where each key is a unique word and its corresponding value is the number of times it appears in the string.
    
    Args:
    s (str): The input string.
    
    Returns:
    dict: A dictionary where each key is a unique word and its corresponding value is the word count.
    """
    # remove punctuation marks and convert string to lowercase
    s = re.sub(r'[^\w\s]', '', s).lower()
    
    # split string into words and count word occurrences
    return dict(Counter(s.split()))