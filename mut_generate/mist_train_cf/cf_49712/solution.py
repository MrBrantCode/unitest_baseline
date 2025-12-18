"""
QUESTION:
Create a function file_name_check that takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise. A file's name is considered valid if it meets the following conditions:
- There should not be more than three digits ('0'-'9') in the file's name, and these digits should not be consecutive.
- The file's name contains exactly one dot '.'.
- The substring before the dot should not be empty, starts with a letter from the latin alphabet ('a'-'z' and 'A'-'Z'), and has at least two letters from the latin alphabet.
- The substring after the dot should be one of these: ['txt', 'exe', 'dll', 'pdf', 'jpeg', 'png', 'zip', 'doc', 'ppt'].
- There should not be any special characters in the file's name.
- The length of the file's name (including the dot) should be between 5 and 100 characters.
"""

def file_name_check(file_name):
    """
    Checks if a file's name is valid based on specific conditions.

    Args:
    file_name (str): The name of the file.

    Returns:
    str: 'Yes' if the file's name is valid, 'No' otherwise.
    """
    # Check if the length of the file's name is between 5 and 100 characters
    if not 5 <= len(file_name) <= 100:
        return 'No'

    # Split the file's name into two parts: before and after the dot
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    name, extension = parts

    # Check if the extension is one of the allowed types
    allowed_extensions = ['txt', 'exe', 'dll', 'pdf', 'jpeg', 'png', 'zip', 'doc', 'ppt']
    if extension not in allowed_extensions:
        return 'No'

    # Check if the name starts with a letter and has at least two letters from the latin alphabet
    if not name[0].isalpha() or sum(c.isalpha() for c in name) < 2:
        return 'No'

    # Check if there are more than three digits or consecutive digits in the name
    digits = [c for c in name if c.isdigit()]
    if len(digits) > 3 or any(digits[i] == digits[i+1] for i in range(len(digits)-1)):
        return 'No'

    # Check if there are any special characters in the name
    if not name.isalnum():
        return 'No'

    return 'Yes'