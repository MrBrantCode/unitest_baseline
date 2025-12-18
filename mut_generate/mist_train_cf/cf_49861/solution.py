"""
QUESTION:
Write a function `find_words(text)` that identifies all the words in a given text string that have more than 4 characters and start with a vowel, and do not contain any repeating consecutive letters. The function should return a list of these words. The input text should be treated as case-insensitive.
"""

import re

def find_words(text):
    vowels = 'aeiou'
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)

    result = []
    for word in words:
        if len(word) > 4 and word[0] in vowels:
            if re.search(r'(.)\1', word) is None:
                result.append(word)

    return result