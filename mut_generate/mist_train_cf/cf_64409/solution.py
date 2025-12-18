"""
QUESTION:
Write a function called `split_sentence_into_lexical_units` that takes a sentence as a string and returns a list of individual words (lexical units) in the sentence, excluding punctuation marks. The function should split the sentence into words based on spaces and remove any punctuation marks from the words.
"""

import string

def split_sentence_into_lexical_units(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    return sentence.split()