"""
QUESTION:
Create a function named `replace_punctuation_with_char` that takes two parameters: `input_string` and `char`. Replace all punctuation in `input_string` with the given `char` and return the result. The function should be efficient enough to handle large amounts of text. The punctuation to be replaced includes at least `.`, `,`, `!`, and `?`.
"""

import string

def replace_punctuation_with_char(input_string, char):
    translator = str.maketrans(string.punctuation, char * len(string.punctuation))
    return input_string.translate(translator)