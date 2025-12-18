"""
QUESTION:
Write a function `capitalize_words` that takes a list of strings as input. The function should capitalize the first letter of each word and convert all remaining letters to lowercase. It should handle strings containing special characters or numbers, leading or trailing spaces, and multiple spaces between words. The function should return a list of strings with the modifications applied.
"""

import re

def capitalize_words(words):
    capitalized_words = []
    for word in words:
        word = word.strip()
        word = re.sub(' +', ' ', word)
        word = word.capitalize()
        capitalized_words.append(word)
    return capitalized_words