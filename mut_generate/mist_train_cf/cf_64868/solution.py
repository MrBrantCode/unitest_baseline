"""
QUESTION:
Write a function `enhanced_file_name_check` that takes a string `file_name` as input and returns 'Yes' if the file name is valid and 'No' if not. A valid file name meets the following conditions: 

- It starts with a latin alphabet letter and has at least two alphabet letters.
- It includes alphanumeric characters with at least one uppercase and lowercase alphabet.
- It includes a maximum of three consecutive digits.
- It includes precisely one '.' that is not at the start and has at least three special characters (excluding the dot) before it.
- The part following the dot is 'txt', 'exe', 'dll', 'pdf', or 'jpeg', and is unique within the name.
- The file name length, including the '.', ranges between 5 and 50 characters.
- The part before the dot does not repeat consecutively.
"""

import re

def enhanced_file_name_check(file_name):
    extension_regex = re.compile('^.*\.(exe|dll|pdf|jpeg|txt)$')
    filename_regex = re.compile('^[a-zA-Z]\w{2,}$')
    alphanumeric_regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?!.*[0-9]{4,})')

    if not 5 <= len(file_name) <= 50:
        return 'No'

    if not extension_regex.match(file_name):
        return 'No'

    filename = file_name.split(".")[0]
    if not filename_regex.match(filename):
        return 'No'

    len_before_alphanumeric_check = len(filename)
    filename = re.sub('\W+', '', filename)
    if len_before_alphanumeric_check - len(filename) < 3 or not alphanumeric_regex.match(filename):
        return 'No'

    return 'Yes'