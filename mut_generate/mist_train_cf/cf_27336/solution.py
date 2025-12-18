"""
QUESTION:
Create a function called `word_frequency` that takes a list of strings as input and returns a dictionary where the keys are unique words from the input list and the values are the frequency of each word. The function should ignore case sensitivity, consider only alphanumeric characters when identifying words, and handle an empty input list by returning an empty dictionary.
"""

import re

def word_frequency(input_list):
    frequency_dict = {}
    for word in input_list:
        cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word.lower())
        if cleaned_word:  
            if cleaned_word in frequency_dict:
                frequency_dict[cleaned_word] += 1
            else:
                frequency_dict[cleaned_word] = 1
    return frequency_dict