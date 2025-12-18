"""
QUESTION:
Implement a function `parse_sentence(sentence)` that takes a sentence as input, extracts words using regular expressions while minimizing the use of built-in functions or libraries, and returns a list of words that do not contain any vowels and have a length of 10 characters or less. The function should be case-insensitive when checking for vowels.
"""

import re

def parse_sentence(sentence):
    words = re.findall(r'\b[A-Za-z]+\b', sentence)  
    filtered_words = []
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for word in words:
        if len(word) <= 10 and not any(vowel in word.lower() for vowel in vowels):
            filtered_words.append(word)

    return filtered_words