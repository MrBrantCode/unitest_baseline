"""
QUESTION:
Write a function `transform_sentence` that takes a string input. The function should return the string in uppercase, with all numerical figures and special characters removed except for exclamation marks, and the order of words reversed. The function should not remove spaces or exclamation marks.
"""

import re

def transform_sentence(sentence):
    # transform to uppercase
    sentence = sentence.upper()

    # eliminate numerical figures and special characters except exclamation marks
    sentence = re.sub(r'[^A-Z! ]+', '', sentence)

    #reverse the order of words
    words = sentence.split() 
    words = words[::-1] 

    return ' '.join(words)