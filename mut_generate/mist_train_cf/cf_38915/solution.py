"""
QUESTION:
Implement a function named `version_up` that takes a file path as input and returns the new file path with the version number incremented by 1. The version number is in the format "_vX" where X is the version number, and it is appended to the file name. If no version number exists in the file name, append "_v1" to indicate the first version.
"""

import re

def version_up(file_path):
    file_name, extension = file_path.split('.')
    match = re.search(r'_v(\d+)$', file_name)
    
    if match:
        version_number = int(match.group(1)) + 1
        new_file_name = re.sub(r'_v\d+$', f'_v{version_number}', file_name)
    else:
        new_file_name = f'{file_name}_v1'
    
    return f'{new_file_name}.{extension}'