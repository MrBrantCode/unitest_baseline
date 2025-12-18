"""
QUESTION:
Write a function `count_words(sentence)` that counts the number of words in a given sentence that begin with a consonant, end with a vowel, have a length less than or equal to 10 characters, and contain at least one uppercase letter.
"""

import re

def count_words(sentence):
    count = 0
    words = sentence.split()
    
    for word in words:
        if re.match(r'^[^aeiouAEIOU]\w*[aeiouAEIOU]$', word) and len(word) <= 10 and any(c.isupper() for c in word):
            count += 1
    
    return count