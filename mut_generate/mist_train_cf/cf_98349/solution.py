"""
QUESTION:
Create a function called `filter_words` that takes a list of words as input. The function should remove all words that have 'e' (either lowercase or uppercase) and return the filtered words in JSON format. The function should be able to handle a large input list efficiently, with a minimum number of iterations, and without considering the case sensitivity of the words.
"""

import json
def filter_words(words):
    return json.dumps([word for word in words if 'e' not in word.lower()])