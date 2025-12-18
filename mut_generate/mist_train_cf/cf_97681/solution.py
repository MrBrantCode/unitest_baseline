"""
QUESTION:
Implement a function named `remove_vowels` that takes a string as input and returns the string with all vowels (both lowercase and uppercase) removed using regular expressions.
"""

import re
def remove_vowels(text):
    pattern = re.compile('[aeiouAEIOU]')
    return re.sub(pattern, '', text)