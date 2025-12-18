"""
QUESTION:
Create a function named `count_extract_sort_number_strings` that takes a string `s` as input and returns two values: the total count of strings that contain numbers (including floating point values) and a sorted list of these number strings in descending order based on their numeric value. The function should ignore case and punctuation marks, and it should work efficiently even for large strings.
"""

import re

def count_extract_sort_number_strings(s):
    number_strings = re.findall(r"\b\d*\.\d+|\b\d+", s)
    sorted_number_strings = sorted(number_strings, key=lambda x: float(x), reverse = True )
    
    return len(number_strings), sorted_number_strings