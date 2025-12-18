"""
QUESTION:
Write a function `kebab_case(sentence)` that takes a sentence as input and returns it in kebab-case. The function should handle non-alphabetic characters by replacing them with a space, split the sentence into words, and join them with hyphens. The function should also handle unexpected inputs: if the input is an empty string, return an empty string; if the input is not a string, return an error message.
"""

import re

def kebab_case(sentence):
    # If input is not of string data type, return an error message
    if not isinstance(sentence, str):
        return 'Input must be a string.'

    # If input is an empty string return an empty string
    if sentence == '':
        return ''

    # Replace non-alphabetic characters with a space
    modified_sentence = re.sub(r'[^A-Za-z0-9 ]', ' ', sentence)

    # Split the sentence into words
    words = modified_sentence.split()

    # Join the words with hyphen and convert to lower case
    kebab_case = "-".join(words).lower()

    return kebab_case