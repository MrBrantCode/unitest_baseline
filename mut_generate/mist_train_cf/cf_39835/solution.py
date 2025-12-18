"""
QUESTION:
Implement a function `is_valid_version` that takes a string as input and returns `True` if the input string represents a valid version number, and `False` otherwise. A valid version number must satisfy the following conditions:
1. It must consist of one or more decimal numbers separated by dots.
2. Each decimal number may contain alphanumeric characters and hyphens, but it cannot start or end with a hyphen.
3. The input string must not contain any leading or trailing spaces.
"""

import re

def is_valid_version(version: str) -> bool:
    if not version or version.strip() != version:
        return False
    
    parts = version.split('.')
    
    for part in parts:
        if not re.match('^[a-zA-Z0-9-]+$', part):
            return False
        if part.startswith('-') or part.endswith('-'):
            return False
    
    return True