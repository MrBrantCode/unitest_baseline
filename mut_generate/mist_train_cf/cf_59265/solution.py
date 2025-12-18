"""
QUESTION:
Construct a function `reverse_text` that takes a string of text as input and returns a string where the sequence of words in the input sentence is rearranged in reverse order. Ensure that any punctuation remains with its original word. The function should disregard any words containing numerical values.
"""

import re

def reverse_text(text):
    # Use regular expressions to find words and punctuation
    words_and_punctuation = re.findall(r'\b\w+\b', text)
    # Exclude words with numbers
    words_and_punctuation = [word for word in words_and_punctuation if not any(char.isdigit() for char in word)]
    # Reverse the words
    words_and_punctuation.reverse()
    # Concatenate the words and return
    return ' '.join(words_and_punctuation)