"""
QUESTION:
Create a function called `validate_password(password)` to check if the input password meets the following requirements: 

- The password must be at least 12 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one special character, and one digit.
- The password must not contain any whitespace characters.
- The password must not contain sequential letters or numbers (e.g. "123", "abc").
- The password must not use more than two same characters consecutively.

Note: The function should return True if the password is valid and False otherwise.
"""

import re

def validate_password(password):
    if (len(password) >= 12 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[\W]', password) and
        re.search(r'\d', password) and
        not re.search(r'\s', password)):
        
        # check for sequence
        for i in range(len(password) - 2):
            if (ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2) or (ord(password[i]) == ord(password[i+1]) + 1 == ord(password[i+2]) + 2):
                return False
        
        # check for repeated characters
        if re.search(r'(.)\1\1', password):
            return False
            
        return True
    else:
        return False