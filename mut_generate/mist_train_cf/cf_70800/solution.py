"""
QUESTION:
Create a function called `complex_file_name_validator` that checks the validity of a given file name based on the following conditions:
- The length of the file name should be between 5 and 50 characters.
- The file name should contain only alphanumeric characters, at least one uppercase letter, one lowercase letter, and one dot.
- The file name should not contain more than three consecutive numbers.
- The file name should have only one dot (.) and the substring before the dot should start with an alphabet and be at least two characters long.
- The file extension should be one of the following: 'txt', 'exe', 'dll', 'pdf', 'jpeg'.
The function should return 'Yes' if all conditions are satisfied, 'No' otherwise.
"""

import re

def complex_file_name_validator(file_name):
    # Check if length of tile name is good
    if len(file_name) < 5 or len(file_name) > 50:
        return 'No'

    # Check for only alphanumeric characters, at least 1 uppercase and lowercase letter and one dot
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\.)[a-zA-Z0-9\.]+$', file_name):
        return 'No'

    # Check for more than three consecutive numbers
    if re.search(r'\d{4,}', file_name):
        return 'No'

    # Check the substring before dot
    split_name = file_name.split('.')

    # Check for multiple extensions
    if len(split_name) != 2:
        return 'No'

    # Check if substring before dot starts with alphabet and of length at least 2
    if not re.match(r'^[a-zA-Z]', split_name[0]) or len(split_name[0]) < 2:
        return 'No'

    # Check for valid extensions
    valid_extensions = ['txt', 'exe', 'dll', 'pdf', 'jpeg']
    if split_name[1] not in valid_extensions:
        return 'No'

    # If all the conditions are satisfied, return 'Yes'
    return 'Yes'