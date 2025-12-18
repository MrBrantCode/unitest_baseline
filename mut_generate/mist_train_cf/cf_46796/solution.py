"""
QUESTION:
Implement a function named `file_name_check` that accepts a string representing a file name. The function should return 'Yes' if the file name is valid and 'No' otherwise. A valid file name meets the following conditions:
- It does not contain more than three digits ('0'-'9').
- It contains exactly one dot '.'.
- The substring before the dot does not contain any empty spaces, starts with a Roman script character ('a'-'z' or 'A'-'Z'), and has at least two Roman script characters.
- The substring after the dot matches one of the following: ['txt', 'exe', 'dll', 'pdf', 'jpeg'].
- The file name length (including the dot) is between 5 and 50 characters (inclusive).
- The function should be case-sensitive when identifying document format identifiers.
"""

import re

def file_name_check(file_name):
    match = re.search(r'^[a-zA-Z]{2,}\.\d{,3}([a-z]{3,4})$',file_name.split('.')[0])
    if match:
        if 5 <= len(file_name) <= 50:
            if match.group(1) in ['txt', 'exe', 'dll', 'pdf', 'jpeg']:
                return 'Yes'
    return 'No'