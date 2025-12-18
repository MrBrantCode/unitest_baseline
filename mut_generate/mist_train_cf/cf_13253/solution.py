"""
QUESTION:
Write a function that captures all the words starting with "A" and ending with a digit. The function should use regular expression to achieve this.
"""

import re

def capture_A_words(s):
    return re.findall(r'\bA\w*\d\b', s)