"""
QUESTION:
Write a function named `common_characters` that takes two strings as input and returns the number of common characters between them. The function should exclude any whitespace, punctuation, and numbers from the comparison and should be able to handle strings in multiple languages and character sets.
"""

import re
def common_characters(str1, str2):
    str1 = re.sub(r'[^\w\s]', '', str1)
    str1 = re.sub(r'\d+', '', str1)
    str2 = re.sub(r'[^\w\s]', '', str2)
    str2 = re.sub(r'\d+', '', str2)
    set1 = set(str1)
    set2 = set(str2)
    common = set1.intersection(set2)
    return len(common)