"""
QUESTION:
Write a function named `replace_cats_with_dogs` that takes a string as input. The function should find and replace all standalone occurrences of the word "cat" with "dog", excluding occurrences of "category" and "caterpillar", and return the modified string.
"""

import re

def replace_cats_with_dogs(string):
    pattern = r'\bcat\b(?!(egory|erpillar))'
    new_string = re.sub(pattern, 'dog', string)
    return new_string