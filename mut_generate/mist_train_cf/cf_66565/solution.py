"""
QUESTION:
Develop a function named `word_frequency` that takes a sentence as input, ignores case sensitivity and punctuation, and returns a dictionary where the keys are the unique words present in the sentence and the values are their frequency of occurrence. The function should be able to handle multiple occurrences of the same word.
"""

import re
from collections import Counter

def word_frequency(sentence):
    # make all words lowercase and remove punctuation
    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence.lower())

    # split the string into a list of words
    word_list = cleaned_sentence.split()

    # use Counter to get the frequency of each word
    frequency_dict = dict(Counter(word_list))

    return frequency_dict