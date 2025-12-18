"""
QUESTION:
Create a function `filter_strings` that takes in a list of strings and an integer `n`. The function should return a new list containing only the strings that meet the following conditions: 
- contain both uppercase and lowercase letters
- have a length greater than or equal to `n`
- do not contain any special characters or numbers.
"""

import re

def filter_strings(strings, n):
    filtered_strings = []
    
    for string in strings:
        if len(string) >= n and re.match("^[a-zA-Z]+$", string) and string.islower() == False and string.isupper() == False:
            filtered_strings.append(string)
    
    return filtered_strings