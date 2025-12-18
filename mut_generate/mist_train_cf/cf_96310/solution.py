"""
QUESTION:
Write a function `find_distinct_words(sentence)` that takes a string `sentence` as input and returns the number of distinct words in the sentence, ignoring case sensitivity and excluding any punctuation marks and common English stop words.
"""

import string

def find_distinct_words(sentence):
    stop_words = ["a", "an", "the", "in", "on", "at", "is", "are", "and", "or", "not", "of", "to", "it", "with"]
    
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = sentence.split()
    words = [word for word in words if word not in stop_words]
    distinct_words = set(words)
    num_distinct_words = len(distinct_words)
    
    return num_distinct_words