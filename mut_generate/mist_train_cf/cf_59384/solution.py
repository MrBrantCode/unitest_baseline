"""
QUESTION:
Create a function named `count_vowel_words` that takes a string `text` as input and returns a dictionary where the keys are the words beginning with a vowel and the values are the counts of those words. The function should be case-insensitive.
"""

import re
from collections import defaultdict

def count_vowel_words(text):
    text = text.lower()
    vowel_words = re.findall(r'\b[aeiou]\w+', text)
    dict_count = defaultdict(int)
    for word in vowel_words:
        dict_count[word] += 1
    return dict_count