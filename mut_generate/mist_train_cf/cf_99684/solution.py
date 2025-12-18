"""
QUESTION:
Write a function called `filter_words` that takes a list of words as input and returns a JSON formatted string containing all the words that do not have the character 'e' (case-insensitive). The function should be efficient enough to handle large lists of more than ten thousand words.
"""

import json
def filter_words(words):
    filtered_words = []
    for word in words:
        if 'e' not in word.lower():
            filtered_words.append(word)
    return json.dumps(filtered_words)