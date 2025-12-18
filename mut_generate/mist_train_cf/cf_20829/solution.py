"""
QUESTION:
Write a function `find_distinct_words(sentence)` that takes a string `sentence` as input, ignores case sensitivity, excludes any punctuation marks, and removes common English stop words from the sentence before counting the distinct words. The function should return the number of distinct words in the sentence.
"""

import string

def find_distinct_words(sentence):
    stop_words = ["a", "an", "the", "in", "on", "at", "is", "are", "and", "or", "not", "of", "to", "it", "with"]
    
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Remove punctuation
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    
    # Split sentence into words
    words = sentence.split()
    
    # Filter out stop words
    words = [word for word in words if word not in stop_words]
    
    # Convert filtered words to set
    distinct_words = set(words)
    
    # Count distinct words
    num_distinct_words = len(distinct_words)
    
    return num_distinct_words