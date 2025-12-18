"""
QUESTION:
Extract the unique alphanumeric words and numbers from a list of mixed data types.

Create a function named `extract_unique_elements` that takes a list of mixed data types as input, where each string element is a word or phrase and numbers are encoded as strings. The function should return two lists: one for unique alphanumeric words and one for unique numbers. 

A string is considered a number if it can be converted into a float. A word is considered alphanumeric if it contains only alphabets and/or digits, case-insensitive. Words and numbers should be considered unique regardless of their original case. Non-alphanumeric characters should be ignored when splitting phrases into individual words.
"""

import re

def extract_unique_elements(input_list):
    number_set = set()
    word_set = set()

    for el in input_list:
        try:
            number = float(el)
            number_set.add(el)
        except ValueError:
            words = re.split(r'\W+', el)
            for word in words:
                if re.search(r'\d', word): 
                    continue
                word = word.lower()
                if len(word) > 0:
                    word_set.add(word)

    return list(number_set), list(word_set)