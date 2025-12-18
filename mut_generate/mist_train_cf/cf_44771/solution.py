"""
QUESTION:
Create a function called `word_frequency` that takes a string of words as input and returns a dictionary. Each key in the dictionary should be a unique word from the input string, and the corresponding value should be the frequency of occurrence of that word in the string. The function should be case-insensitive and ignore punctuation when counting word frequencies.
"""

import re

def word_frequency(input_string):
    cleaned_string = re.sub(r'\W+', ' ', input_string).lower()
    word_list = cleaned_string.split()
    word_freq = {word: word_list.count(word) for word in set(word_list)}
    return word_freq