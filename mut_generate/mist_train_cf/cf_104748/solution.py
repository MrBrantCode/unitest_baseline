"""
QUESTION:
Write a function `format_slug` that takes a string as input, removes any special characters and punctuation marks, replaces spaces with hyphens, and converts the resulting string to lowercase. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

import re

def format_slug(string):
    # remove special characters and punctuation marks
    slug = re.sub(r'[^\w\s-]', '', string)
    # replace spaces with hyphens
    slug = slug.replace(' ', '-')
    # convert to lowercase
    slug = slug.lower()
    return slug