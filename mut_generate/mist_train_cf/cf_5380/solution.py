"""
QUESTION:
Write a function called `count_words` that takes a sentence as input and returns the number of words that meet the following conditions:
- The word starts with a consonant (any letter other than a, e, i, o, or u, regardless of case).
- The word ends with a vowel (a, e, i, o, or u, regardless of case).
- The word's length is less than or equal to 10 characters.
- The word contains at least one uppercase letter.

Assume the input sentence only contains spaces as word separators and does not contain punctuation.
"""

import re

def count_words(sentence):
    count = 0
    words = sentence.split()
    
    for word in words:
        if re.match(r'^[^aeiouAEIOU]\w*[aeiouAEIOU]$', word) and len(word) <= 10 and any(c.isupper() for c in word):
            count += 1
    
    return count