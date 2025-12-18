"""
QUESTION:
Create a function named `check_patterns` that takes a string `text` as input and checks if any lines in the text end with "py", "java", "php", or "cpp" (case-insensitive). The function should return a boolean value indicating whether any of these patterns were found at the end of any line.
"""

import re

def check_patterns(text):
    """
    Checks if any lines in the text end with "py", "java", "php", or "cpp" (case-insensitive).
    
    Args:
        text (str): The input text to be checked.
    
    Returns:
        bool: True if any of the patterns were found at the end of any line, False otherwise.
    """
    patterns = [r'py$', r'java$', r'php$', r'cpp$']
    text_lines = text.lower().split('\n')

    for line in text_lines:
        for pattern in patterns:
            if re.search(pattern, line):
                return True

    return False