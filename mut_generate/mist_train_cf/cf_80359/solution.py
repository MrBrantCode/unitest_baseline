"""
QUESTION:
Write a function `count_words_starting_with_vowel(text)` that takes a string `text` as input and returns a dictionary where the keys are unique words that start with a vowel (either uppercase or lowercase) and the values are their respective frequencies in the text. The function should be case-insensitive.
"""

import re
from collections import defaultdict

def count_words_starting_with_vowel(text):
    regex = r'\b[aeiouAEIOU]\w*' 
    words = re.findall(regex, text)
 
    frequency = defaultdict(int)
    for word in words:
        frequency[word.lower()] += 1
  
    return frequency