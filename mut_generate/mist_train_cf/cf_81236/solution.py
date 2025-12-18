"""
QUESTION:
Create a function called `file_name_check` that takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise. The file's name is valid if all of the following conditions are met:
- There are not more than three digits in the file's name.
- The file's name contains exactly one dot '.'.
- The substring before the dot is not empty, starts with a letter from the latin alphabet, and has at least two letters from the latin alphabet.
- The substring after the dot is one of these: ['txt', 'exe', 'dll', 'pdf', 'jpeg'].
- The length of the file's name (including the dot) is between 5 and 50 characters.
- The function should support case sensitivity for both the part before and after the dot.
"""

def file_name_check(file_name):
    """
    Checks if a file name is valid based on the given conditions.
    
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, starts with a letter from 
    the latin alphabet ('a'-'z' and 'A'-'Z'), and has at least two letters from the latin alphabet.
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll', 'pdf', 'jpeg']
    - The length of the file's name (including the dot) should be between 5 and 50 characters.
    - The function should support case sensitivity for both the part before and after the dot.

    Parameters:
    file_name (str): The name of the file to be checked.

    Returns:
    str: 'Yes' if the file name is valid, 'No' otherwise.
    """
    import re

    if not 5 <= len(file_name) <= 50:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    file_parts = file_name.split('.')
    file_name_part, file_extension = file_parts[0], file_parts[1]

    if not re.match("^[A-Za-z][A-Za-z\d]{1,}$", file_name_part):
        return 'No'

    if file_extension not in ['txt', 'exe', 'dll', 'pdf', 'jpeg']:
        return 'No'

    return 'Yes'