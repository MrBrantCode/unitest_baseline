"""
QUESTION:
Write a function `count_distinct_words(sentence)` that takes a string `sentence` as input and returns the number of distinct words in the sentence, ignoring case sensitivity and excluding any punctuation marks. The function should consider different cases of the same word as the same word and exclude any non-alphanumeric characters except for spaces.
"""

import string

def count_distinct_words(sentence):
    distinct_words = set()
    
    # Convert sentence to lowercase
    sentence = sentence.lower()
    
    # Remove punctuation marks
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    
    # Split sentence into words
    words = sentence.split()
    
    # Add distinct words to the set
    for word in words:
        distinct_words.add(word)
    
    return len(distinct_words)