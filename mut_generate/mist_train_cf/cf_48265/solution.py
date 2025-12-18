"""
QUESTION:
Create a function named `count_unique_words` that takes a sentence as input. The function should return a list of tuples, where each tuple contains a unique word from the sentence and its occurrence count. The function should be case-insensitive, remove all punctuation marks from the sentence before counting, and sort the result in descending order of occurrence count. If two words have the same occurrence count, they should be sorted alphabetically.
"""

import re
from collections import Counter

def count_unique_words(sentence):
    # removing punctuation
    clean_sentence = re.sub(r'[^\w\s]', '', sentence)

    # splitting sentence into a list of words, case-insensitive
    word_list = clean_sentence.lower().split()

    # creating a dictionary where keys are unique words and values are their counts
    word_count = Counter(word_list)

    # creating a list of tuples [(word, count), ..., (word, count)]
    word_count_list = [(k, v) for k, v in word_count.items()]

    # sorting the list first alphabetically, then by count (descending) 
    unique_words = sorted(sorted(word_count_list), key=lambda x: x[1], reverse=True)
    
    return unique_words