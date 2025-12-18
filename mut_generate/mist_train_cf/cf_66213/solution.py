"""
QUESTION:
Write a Python function named `process_text` that takes two parameters: `input_text` and `stop_words` (defaulting to `None` if not provided). The function should split the `input_text` into individual sentences and then into words, removing any punctuation and special characters without using any external libraries for this purpose. It should also exclude any words found in the `stop_words` list. The function should handle edge cases such as empty strings, strings with only spaces, or strings with only special characters, and return an empty list for these cases.
"""

import re

def process_text(input_text, stop_words=None):
    if stop_words is None:
        stop_words = []  

    sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', input_text)

    words_in_sentences = []
    
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence)
        words = [word for word in words if word.lower() not in stop_words]
        if words:
            words_in_sentences.append(words)

    return words_in_sentences