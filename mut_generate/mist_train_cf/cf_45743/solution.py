"""
QUESTION:
Write a function `validate_file_name` that checks if a given `file_name` complies with a certain naming policy. The policy rules are:
- The name must not contain any of the reserved Windows characters `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, `*`
- The length of the name must be within 5 to 50 characters.
- The name must be separated into two parts by exactly one dot. The first part is the base name of the file, and the second part is the file extension.
- In the base name part, it must start with a letter, and the remaining characters can be letters or digits. It must contain at least one uppercase letter, one lowercase letter, and it must not contain a sequence of 4 or more digits.
- The file extension must be one of: `txt`, `exe`, `dll`, `pdf`, and `jpeg`.
"""

import re

def validate_file_name(file_name):
    # Check for the reserved Windows characters
    reserved_chars = {'<', '>', ':', '"', '/', '\\', '|', '?', '*'}
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
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', name) \
       or not any(c.isupper() for c in name) \
       or not any(c.islower() for c in name) \
       or len(re.findall(r'\d{4,}', name)) > 0:
        return 'No'
    # Check the conditions for the extension part
    if extension not in ['txt', 'exe', 'dll', 'pdf', 'jpeg']:
        return 'No'
    return 'Yes'