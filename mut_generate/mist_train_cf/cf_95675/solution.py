"""
QUESTION:
Write a function `replace_cats_with_dogs(string)` that takes a string as input and returns a new string where all standalone occurrences of "cat" are replaced with "dog". The replacement should not affect words that contain "cat" as a substring, such as "category" and "caterpillar".
"""

import re

def replace_cats_with_dogs(string):
    pattern = r'\bcat\b(?!(egory|erpillar))'
    new_string = re.sub(pattern, 'dog', string)
    return new_string