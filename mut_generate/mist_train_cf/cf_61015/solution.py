"""
QUESTION:
Write a function called `last_two_words` that takes a string of words as input and returns the last two words from the string, excluding punctuation and special characters except for apostrophes within words. If the string contains only one word, return that word. The function should be efficient and handle large strings with a time complexity of O(n).
"""

import re

def last_two_words(string):
    clean_string = re.sub(r'[^\w\s\']','', string)
    words = clean_string.split()
    
    if len(words) < 2:
        return words[0] if words else ''
    else:
        return ' '.join(words[-2:])