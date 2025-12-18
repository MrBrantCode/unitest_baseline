"""
QUESTION:
Create a function called `replace_punctuation` that takes two parameters: `input_string` and `replace_char`. The function should replace all punctuation in `input_string` with `replace_char` and return the resulting string along with a dictionary containing the count of each punctuation mark replaced. The function should not use the built-in `replace()` or `translate()` functions.
"""

import string

def replace_punctuation(input_string, replace_char):
    punctuation_count = {}
    new_string = ''.join([char if char not in string.punctuation else replace_char for char in input_string])
    
    for char in input_string:
        if char in string.punctuation:
            if char in punctuation_count:
                punctuation_count[char] += 1
            else:
                punctuation_count[char] = 1
    
    return new_string, punctuation_count