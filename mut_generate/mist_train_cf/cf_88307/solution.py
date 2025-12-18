"""
QUESTION:
Create a function named `validate_string` that checks if a given string meets the following conditions: 
- length between 6 and 20 characters (inclusive)
- contains at least one uppercase letter, one lowercase letter, and one numeric digit
- does not contain any special characters
- does not start or end with a digit
- does not contain consecutive repeated characters (more than two)
- does not contain more than three consecutive uppercase or lowercase letters.
"""

import re

def validate_string(string):
    # Check length
    if len(string) < 6 or len(string) > 20:
        return False
    
    # Check if string contains at least one uppercase, lowercase, and numeric digit
    if not re.search(r'[A-Z]', string) or not re.search(r'[a-z]', string) or not re.search(r'\d', string):
        return False
    
    # Check for special characters
    if re.search(r'[^a-zA-Z0-9]', string):
        return False
    
    # Check if string starts or ends with a digit
    if string[0].isdigit() or string[-1].isdigit():
        return False
    
    # Check for consecutive repeated characters
    for i in range(len(string)-2):
        if string[i] == string[i+1] and string[i+1] == string[i+2]:
            return False
    
    # Check for more than three consecutive uppercase or lowercase letters
    if re.search(r'[A-Z]{4,}|[a-z]{4,}', string):
        return False
    
    return True