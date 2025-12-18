"""
QUESTION:
Create a function `verify_phoenix` that verifies if the word "phoenix" (case-sensitive) is at the start of a single-line string and is the only capitalized word until the end of the string. The function should return `True` if the condition is met, `False` otherwise. The function should not handle multi-line strings or edge cases such as additional spaces or special characters.
"""

import re

def verify_phoenix(text):
    pattern = r'^Phoenix[^A-Z]*$'
    return bool(re.match(pattern, text))