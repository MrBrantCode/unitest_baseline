"""
QUESTION:
Write a function named `find_seq` that takes a string `text` as input and returns all substrings that meet the following criteria: 
- Start with a lowercase letter 'a'
- Contain at least one numeric digit
- Contain at least one special character (excluding alphanumeric characters)
- End with an uppercase letter 'Z'
"""

import re

def find_seq(text):
    pattern = r'^a(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:"|,.<>\/?]).*Z$'
    result = re.findall(pattern, text)
    return result