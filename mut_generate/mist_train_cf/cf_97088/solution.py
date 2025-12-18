"""
QUESTION:
Write a function named `count_word_frequency` that takes three parameters: a string, a list of words, and a list of stopwords. The function should count the frequency of each word in the list that appears in the string, ignoring punctuation marks and case differences. The function should return a dictionary where the keys are the words and the values are their frequency counts in descending order. The function should exclude stopwords from the count.
"""

import re

def count_word_frequency(string, word_list, stopwords):
    # Convert string to lowercase
    string = string.lower()
    
    # Split string into words
    words = string.split()
    
    # Remove punctuation marks from each word
    words = [re.sub(r'[^\w\s]', '', word) for word in words]
    
    # Remove stopwords from word list
    word_list = [word.lower() for word in word_list if word.lower() not in stopwords]
    
    # Create dictionary to store frequency count
    frequency_count = {}
    
    # Iterate over words and update frequency count
    for word in words:
        if word in word_list:
            if word in frequency_count:
                frequency_count[word] += 1
            else:
                frequency_count[word] = 1
    
    # Sort dictionary by frequency count in descending order
    sorted_frequency_count = {k: v for k, v in sorted(frequency_count.items(), key=lambda item: item[1], reverse=True)}
    
    return sorted_frequency_count