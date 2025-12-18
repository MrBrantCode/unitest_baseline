"""
QUESTION:
Implement a function named `split_reverse_sentence` that takes in a sentence as a string, splits it into words using regular expressions, and returns the words in reverse order. The function should not use any built-in string or array manipulation functions, such as `split()`, `reverse()`, or indexing. It should handle leading and trailing whitespaces in the sentence and multiple consecutive whitespaces between words.
"""

import re

def split_reverse_sentence(sentence):
    # Remove leading and trailing whitespaces
    sentence = re.sub(r'^\s+|\s+$', '', sentence)

    # Split sentence into words using regular expression
    words = re.findall(r'\S+', sentence)

    # Reverse the order of the words
    for i in range(len(words) // 2):
        words[i], words[len(words) - i - 1] = words[len(words) - i - 1], words[i]

    return words