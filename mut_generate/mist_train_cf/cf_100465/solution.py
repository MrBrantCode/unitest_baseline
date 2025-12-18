"""
QUESTION:
Write a function called `remove_vowels` that takes a string as input and returns a new string with all vowels (both lowercase and uppercase) removed. The function should use regular expressions to achieve this.
"""

import re

def remove_vowels(text):
    pattern = re.compile('[aeiouAEIOU]')
    return re.sub(pattern, '', text)