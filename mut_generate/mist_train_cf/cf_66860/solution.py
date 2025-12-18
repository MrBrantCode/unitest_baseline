"""
QUESTION:
Write a function `word_positions(text, word_list)` that takes a sentence `text` and a list of words `word_list` as input, and returns a dictionary where the keys are the words from `word_list` and the values are lists of their corresponding positions in the sentence. The positions should be calculated based on the word order, starting from 1, and should ignore punctuation, special characters, and multiple occurrences of the same word.
"""

import re

def word_positions(text, word_list):
    cleaned_text = re.sub(r'[^\w\s]','',text)
    text_list = cleaned_text.split()
    word_position = {word:[i+1 for i, x in enumerate(text_list) if x == word] for word in word_list}
    return word_position