"""
QUESTION:
Create a function called `count_punctuation(text)` that takes a string `text` as input and returns a dictionary where the keys are unique Unicode punctuation characters and the values are their corresponding counts in the input text. The function should use the `unicodedata` module to identify punctuation characters.
"""

import unicodedata

def count_punctuation(text):
    punctuation_dict = {}
    for char in text:
        if unicodedata.category(char)[0] == 'P': 
            if char in punctuation_dict:
                punctuation_dict[char] += 1
            else:
                punctuation_dict[char] = 1
    return punctuation_dict