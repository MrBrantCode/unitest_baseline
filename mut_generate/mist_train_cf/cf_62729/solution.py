"""
QUESTION:
Compose a function named `find_terms` to identify a string of characters that contains the terms "hello" and "world" in this exact order, regardless of their adjacency and case sensitivity. The function should return `True` if both terms are found and `False` otherwise.
"""

import re

def find_terms(string):
    pattern = r'hello.*world'
    match = re.search(pattern, string, re.IGNORECASE)
    if match:
        return True
    else:
        return False