"""
QUESTION:
Create a function called `longest_string` that takes a list of strings as input and returns the longest string in the list. The function should return the first occurrence of the longest string if there are multiple strings of the same maximum length. If the input list is empty or contains only whitespace strings, or if all strings contain special characters or numbers, the function should return None.
"""

import re

def longest_string(input_list):
    if not input_list or all(s.isspace() for s in input_list):
        return None
    
    input_list = [s.strip() for s in input_list]
    input_list = [s for s in input_list if re.match('^[a-zA-Z]+$', s)]
    
    if not input_list:
        return None
    
    longest = input_list[0]
    for s in input_list:
        if len(s) > len(longest):
            longest = s
    
    return longest