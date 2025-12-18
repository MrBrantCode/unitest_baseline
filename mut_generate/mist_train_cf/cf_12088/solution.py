"""
QUESTION:
Write a function `get_most_frequent_word` that takes a list of words as input and returns the most frequently used word(s). The function should ignore case, punctuation marks, and special characters, and handle large input lists efficiently. If there are multiple words with the same highest frequency, return all of them. The function should also handle edge cases such as empty lists, lists containing only empty strings, special characters, numbers, or mixed data types, and return an appropriate error message.
"""

import re
from collections import Counter

def get_most_frequent_word(words):
    # Check for empty list
    if len(words) == 0:
        return "Error: List is empty"
    
    # Check for list containing only empty strings
    if all(word == '' for word in words):
        return "Error: List contains only empty strings"
    
    # Check for list containing only special characters or punctuation marks
    if all(re.match(r'^\W+$', word) for word in words):
        return "Error: List contains only special characters or punctuation marks"
    
    # Check for list containing only numbers
    if all(re.match(r'^[0-9]+$', word) for word in words):
        return "Error: List contains only numbers"
    
    # Check for list with mixed data types
    if any(isinstance(word, (int, float)) for word in words) or any(re.match(r'^\W+$', word) for word in words):
        return "Error: List contains mixed data types"
    
    # Remove punctuation marks and convert words to lowercase
    words = [re.sub(r'[^\w\s]', '', word).lower() for word in words]
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Find the maximum frequency
    max_frequency = max(word_counts.values())
    
    # Check if all words have the same frequency
    if len(set(word_counts.values())) == 1:
        return "Error: All words have the same frequency"
    
    # Find the most frequently used words
    most_frequent_words = [word for word, count in word_counts.items() if count == max_frequency]
    
    return most_frequent_words