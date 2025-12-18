"""
QUESTION:
Create a function named `refined_list_summation` that accepts a list of strings and an optional boolean parameter `inverse` defaulting to `False`. The function should filter out strings containing numerical digits and sort the remaining strings by their length in ascending order (or descending if `inverse` is `True`). If multiple strings have the same length, they should be sorted alphabetically in a case-insensitive manner. The function should return the sorted list of strings.
"""

import re

def refined_list_summation(lst, inverse=False):
    lst = [s for s in lst if not any(i.isdigit() for i in s)]  # Remove elements that contain digit
    return sorted(lst, key=lambda s: (len(s), s.lower()), reverse=inverse) 
    # sort by length, then by alphabet (case insensitive) and reverse if inverse=True