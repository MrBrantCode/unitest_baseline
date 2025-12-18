"""
QUESTION:
Write a function `is_consecutive(sequence)` that checks if a given string contains a sequence of 5 consecutive numbers, regardless of order or position in the string. The function should return `True` if such a sequence exists and `False` otherwise.
"""

import re

def is_consecutive(sequence):
    matches = re.findall(r'(\d{5})', sequence)
    
    for match in matches:
        digits = [int(d) for d in match]
        
        if sorted(digits) == list(range(min(digits), max(digits)+1)):
            return True
    return False