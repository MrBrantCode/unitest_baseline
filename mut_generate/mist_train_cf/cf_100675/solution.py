"""
QUESTION:
Create a function called `filter_words` that takes a list of spelling words as input and returns a JSON-formatted list of words that do not contain the letter 'e' (case-insensitive). The function should have a time complexity of O(n), where n is the number of words in the input list, and should be able to handle large input lists efficiently.
"""

import json
def filter_words(words):
    filtered_words = []
    for word in words:
        if 'e' not in word.lower():
            filtered_words.append(word)
    return json.dumps(filtered_words)