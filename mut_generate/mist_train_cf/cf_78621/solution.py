"""
QUESTION:
Write a function named `dog_cat_x_finder` that takes a string as input and returns the total count of "CAT" occurrences in the words or phrases that match the following pattern: 
- start with "dog" 
- followed by any number of uppercase letters 
- have "CAT" anywhere in the middle with an arbitrary number of occurrences 
- include only uppercase letters except for the initial "dog" 
- terminate with "X".
"""

import re

def dog_cat_x_finder(string):
    pattern = re.compile(r'^dog[A-Z]*(CAT[A-Z]*)*X$')
    matches = re.finditer(pattern, string)

    cat_count = 0
    for match in matches:
        sub_pattern = re.compile(r'CAT')
        sub_matches = re.finditer(sub_pattern, match.group())
        for _ in sub_matches:
            cat_count+=1
    
    return cat_count