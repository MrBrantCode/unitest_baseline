"""
QUESTION:
Implement a function named `string_to_dict(s)` that takes a string `s` as input, where the string contains sentences separated by the pipe ("|") character. The function should split these sentences into words, excluding punctuation and converting to lower case, and store them in a dictionary where each sentence corresponds to a list of words.
"""

import string

def string_to_dict(s):
    sentences = s.split("|")
    dict_sentences = {}
    for sentence in sentences:
        words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
        dict_sentences[sentence] = words
    return dict_sentences