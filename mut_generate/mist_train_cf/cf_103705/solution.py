"""
QUESTION:
Write a function named `count_word_occurrences` that uses regular expression to identify words in a given string and returns a dictionary where the keys are the words and the values are their corresponding counts. The function should be case-insensitive and should ignore punctuation and numbers.
"""

import re
from collections import Counter

def count_word_occurrences(string):
    """
    This function uses regular expression to identify words in a given string 
    and returns a dictionary where the keys are the words and the values are their corresponding counts.
    
    The function is case-insensitive and ignores punctuation and numbers.
    
    Parameters:
    string (str): The input string to count word occurrences from.
    
    Returns:
    dict: A dictionary where the keys are the words and the values are their corresponding counts.
    """
    
    # Remove punctuation and convert to lowercase
    cleaned_string = re.sub(r'[^\w\s]', '', string.lower())
    
    # Find all words in the string
    words = re.findall(r'\b\w+\b', cleaned_string)
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    return dict(word_counts)