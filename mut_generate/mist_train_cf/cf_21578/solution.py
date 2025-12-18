"""
QUESTION:
Create a function `validate_text(text)` that takes a string `text` as input and returns `True` if it meets the following conditions, otherwise returns `False`: 
- The text must contain at least one uppercase letter and one lowercase letter.
- The text must include at least one special character (!, @, #, $, %, &, or *).
- The text must include at least one digit (0-9).
- The text must be at least 10 characters long and no more than 30 characters long.
"""

import re

def validate_text(text):
    # Check for at least one uppercase letter and one lowercase letter
    if not any(char.isupper() for char in text) or not any(char.islower() for char in text):
        return False
    
    # Check for at least one special character
    if not re.search(r'[!@#$%&*]', text):
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in text):
        return False
    
    # Check for text length between 10 and 30 characters
    if len(text) < 10 or len(text) > 30:
        return False
    
    return True