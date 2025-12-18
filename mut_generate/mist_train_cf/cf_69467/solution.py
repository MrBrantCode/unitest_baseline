"""
QUESTION:
Create a function `file_name_check(file_name)` that takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise. A file's name is considered valid if it meets the following conditions: 
- contains alphanumeric characters and has at least one uppercase and one lowercase alphabet
- does not have more than three consecutive digits
- contains exactly one dot '.'
- the substring before the dot is not empty, starts with a letter from the Latin alphabet, and has at least two letters from the Latin alphabet
- the substring after the dot is one of ['txt', 'exe', 'dll', 'pdf', 'jpeg']
- the extension appears only once in the file's name
- the length of the file's name (including the dot) is between 5 and 50 characters.
"""

import re

def file_name_check(file_name):
    # Check if file_name is of valid length
    if len(file_name) < 5 or len(file_name) > 50:
        return 'No'

    # Check if there is exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'

    # Split file_name into string before and after the dot
    file_name_split = file_name.split('.')

    # Check if the substring before the dot is valid
    if not re.match("^[a-zA-Z][a-zA-Z0-9]*$", file_name_split[0]) or not re.search("(?=.*[a-z])(?=.*[A-Z])", file_name_split[0]):
        return 'No'

    # Check if there should be a consecutive sequence of more than three digits
    if re.search(r'\d\d\d\d+', file_name_split[0]):
        return 'No'

    # Check if the substring after the dot is valid and one of the allowed extensions
    if file_name_split[1] not in ['txt', 'exe', 'dll', 'pdf', 'jpeg']:
        return 'No'

    # If all conditions are satisfied, return 'Yes'
    return 'Yes'