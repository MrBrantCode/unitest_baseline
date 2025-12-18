"""
QUESTION:
Design a function named `reverse_words` that takes a string as input, removes non-alphabet characters, reverses the order of words, and excludes consecutive duplicates. The function should return a string with the processed words. The input string may contain non-alphabet characters and consecutive duplicate words.
"""

import re

def reverse_words(string):
    string = re.sub('[^a-zA-Z ]', '', string)  # Remove non-alphabet characters
    words = string.split()  # Split string into words
    words.reverse()  # Reverse the order of words
    result = []
    previous_word = None
    for word in words:
        if word == previous_word:
            continue
        result.append(word)
        previous_word = word
    return ' '.join(result)  # Join words into a string