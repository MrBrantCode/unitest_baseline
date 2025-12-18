"""
QUESTION:
Implement a function `file_name_check(file_name)` that takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise. The file's name is valid if it meets the following conditions:

- Contains alphanumeric characters with at least one uppercase and one lowercase alphabet.
- Has a maximum of three consecutive digits ('0'-'9').
- Has exactly one dot '.'.
- The substring before the dot is not empty, starts with a latin alphabet letter ('a'-'z' and 'A'-'Z'), and has at least two latin alphabet letters.
- The substring after the dot is one of ['txt', 'exe', 'dll', 'pdf', 'jpeg'] and is unique within the name.
- The file's name length, including the dot, is between 5 and 50 characters.
"""

import re

def file_name_check(file_name):
    # Check if the file's name length is within the allowed range
    if not 5 <= len(file_name) <= 50:
        return "No"
    
    name, dot, extension = file_name.rpartition('.')
    
    # Check if the file's name has exactly one dot and a valid extension
    if not dot or extension not in ['txt', 'exe', 'dll', 'pdf', 'jpeg']:
        return "No"
    
    # Check if the file's name has valid alphanumeric characters, and has at least
    # one uppercase, one lowercase, and maximum of three consecutive digits
    if not (re.match(r'[A-Za-z].*$', name) and
            re.search(r'[A-Z]', name) and
            re.search(r'[a-z]', name) and
            not re.search(r'\d{4,}', name)):
        return "No"
    
    # Check if the file's name has exactly two latin alphabet letters
    if len(re.findall(r'[A-Za-z]', name)) < 2:
        return "No"
    
    return "Yes"