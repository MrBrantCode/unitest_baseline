"""
QUESTION:
Develop a function named `count_words` that takes a string as input and returns the number of words present in the string. Each word should be at least 3 characters long and consist only of alphabetic characters, but may contain hyphens or apostrophes. The function should ignore leading or trailing spaces and punctuation marks such as periods, exclamation marks, question marks, or commas.
"""

import re

def count_words(string):
    string = re.sub(r'[^\w\s-]', '', string)
    return sum(1 for word in string.split() if len(word) >= 3 and word.replace('-', '').replace("'", "").isalpha())