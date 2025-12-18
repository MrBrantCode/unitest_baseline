"""
QUESTION:
Create a function called `decode_string` that takes two parameters: a string and a dictionary. The string can contain plain English words and coded words, and the dictionary maps coded words to their English translations. The function should return the input string with all plain English words converted to uppercase and coded words decoded and then converted to uppercase, while preserving punctuation and handling edge cases such as punctuations and digits within words.
"""

import string

def decode_string(input_s, dictionary):
    punctuation = string.punctuation
    output_s = ''
    for word in input_s.split():
        clean_word = ''.join(e for e in word if e.isalnum())
        punct = ''.join(e for e in word if e in punctuation)
        decoded_word = dictionary.get(clean_word, clean_word)
        output_s += decoded_word.upper() + punct + ' '
    return output_s.rstrip()