"""
QUESTION:
Create a function `count_word_occurrences(text, word)` that counts the occurrences of a given word in a text string, excluding any occurrences inside quoted strings or comments. The function should return the count of occurrences of the word.
"""

import re

def count_word_occurrences(text, word):
    # Remove quoted strings
    text = re.sub(r'\'[^\']*\'', '', text)  # remove single quoted strings
    text = re.sub(r'\"[^\"]*\"', '', text)  # remove double quoted strings

    # Remove comments
    text = re.sub(r'#.*', '', text)  # remove comments

    # Count occurrences of the word
    count = len(re.findall(r'\b{}\b'.format(word), text))

    return count