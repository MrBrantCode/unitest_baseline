"""
QUESTION:
Create a function `intricate_word_sequence(s, target)` that takes a string `s` and a target word `target` as input. The string `s` contains words separated by one or more non-alphabetic characters. The function should return a tuple where the first element is a list of words in the original order, excluding the target word, and the second element is a dictionary with each word's occurrence count in the string.
"""

import re

def intricate_word_sequence(s, target):
    # use regex to split string into words
    words = re.findall(r'\b\w+\b', s)
    
    # initialize an empty dictionary for word counts
    dictionary = {}
    
    # process each word
    for word in words:
        # skip the target word
        if word == target: continue
        
        # increment the word count
        dictionary[word] = dictionary.get(word, 0) + 1

    # filter out target words and return results
    return ([word for word in words if word != target], dictionary)