"""
QUESTION:
Write a function `eradicate_and_reverse(sentence)` that takes a string as input, removes surplus spacing between words while maintaining uniform intervals, reverses the order of the words, and properly handles punctuation and symbols. The function should return the modified sentence.
"""

import re

def eradicate_and_reverse(sentence):
    # Eradicate the surplus spacing.
    sentence = re.sub(" +", " ", sentence)

    # Reverse the order of the words in the sentence.
    words = sentence.split(' ')
    sentence = ' '.join(reversed(words))

    # Handle punctuation and symbols properly.
    sentence = re.sub(" ,", ",", sentence)
    sentence = re.sub(" -", "-", sentence)
    sentence = re.sub(" !", "!", sentence)

    return sentence