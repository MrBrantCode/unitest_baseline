"""
QUESTION:
Create a function `detect_sequence` that takes a string as input and returns True if the string starts with an uppercase 'M', ends with a lowercase 'x', and contains at least one digit and one special character, and False otherwise. The special characters to consider are !, @, #, $, %, ^, &, *, (, ), _, +, -, {, }, [, ], \, :, ;, ', <, >, ., ?, and /. The digit and special character can be in any position within the string, but the string must start with 'M' and end with 'x'.
"""

import re

def detect_sequence(string):
    pattern = r"M.*[0-9].*[!@#\$%\^&\*\(\)_\+\-=\{\}\[\]\\\|:;'<,>.?/].*x$"
    if re.match(pattern, string):
        return True
    return False