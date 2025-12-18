"""
QUESTION:
Create a function named `file_name_check` that takes a string denoting a file name and returns 'Yes' if the name is valid; otherwise, 'No'. The file name is valid if it meets the following conditions:

- It contains alphanumeric characters, with at least one uppercase and lowercase character.
- It contains a maximum of three consecutive digits ('0'-'9').
- It contains exactly one dot '.'.
- The substring before the dot is not null, starts with a latin alphabet letter ('a'-'z', 'A'-'Z'), and has at least two latin alphabet letters.
- The substring following the dot is one of ['txt', 'exe', 'dll', 'pdf', 'jpeg'].
- The extension is unique in the name.
- The file name, including the dot, is between 5 to 50 characters long.
- It does not contain any reserved Windows characters: <, >, :, ", /, \, |, ?, *.
"""

import re

def file_name_check(file_name):
    # Check for the reserved Windows characters
    reserved_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    if any(c in file_name for c in reserved_chars):
        return 'No'
    # Check for the length requirement
    if not (5 <= len(file_name) <= 50):
        return 'No'
    # Check if the file name has exactly one dot and get the name and extension parts
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    name, extension = parts
    # Check the conditions for the name part
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', name) or not any(c.isupper() for c in name) or not any(c.islower() for c in name) or len(re.findall(r'\d{4,}', name)) > 0:
        return 'No'
    # Check the conditions for the extension part
    if extension not in ['txt', 'exe', 'dll', 'pdf', 'jpeg']:
        return 'No'
    return 'Yes'