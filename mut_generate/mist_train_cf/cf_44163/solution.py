"""
QUESTION:
Create a function named `extract_data(s)` that takes a string `s` as input. The function should return a list of words separated by either whitespace, semicolons, or commas. If none of these separators exist in the string, the function should return the count of upper-case alphabetic characters with an odd index (ord('A') = 0, ord('B') = 1, ... ord('Z') = 25).
"""

import re

def extract_data(s):
    data = re.split(' |;|,', s)
  
    if len(data) > 1:
        return data
    
    count = sum(1 for c in s if c.isupper() and (ord(c) - ord('A')) % 2 != 0)
  
    return count