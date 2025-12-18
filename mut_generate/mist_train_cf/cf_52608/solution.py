"""
QUESTION:
Create a function named analyze_text that isolates every individual lexical unit from a complex paragraph and stores them into a linear data structure. The function should include both a count of each unique lexical unit and the position of each lexical unit within the original text. Ensure the solution can handle numerous punctuation marks, whitespace variations, as well as capitalized and un-capitalized words.
"""

import string
import re

def analyze_text(paragraph):
    raw_words = re.split('\W+', paragraph)
    words = [word.lower() for word in raw_words if word]

    word_data = {} 
    for index, word in enumerate(words):
        if word not in word_data:
            word_data[word] = {'count': 1, 'positions': [index]}
        else:
            word_data[word]['count'] += 1
            word_data[word]['positions'].append(index)

    return word_data