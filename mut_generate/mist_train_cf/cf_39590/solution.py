"""
QUESTION:
Implement a function `normalize_answer(s)` that takes a string `s` as input, converts it to lowercase, removes punctuation and articles ("a", "an", "the"), and removes extra whitespace. Use the helper functions `remove_articles(text)` and `white_space_fix(text)` to remove articles and fix whitespace, respectively. Ensure the function handles these operations in the correct order to achieve the desired text normalization.
"""

import re

def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text.lower())

    def white_space_fix(text):
        return ' '.join(text.split())

    s = remove_articles(re.sub(r'[^\w\s]', '', s.lower()))
    return white_space_fix(s)