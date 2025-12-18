"""
QUESTION:
Write a function named `validate_password` that checks if a given password is valid based on the following rules: 
- The password must have at least 8 characters.
- The password must have at least one uppercase letter.
- The password must have at least one lowercase letter.
- The password must have at least one number.
- The password must have at least one special character.
The function should print an informative error message for each failed condition and return False if any condition is not met. If all conditions are met, the function should return True.
"""

import re

def validate_password(password): 
    if len(password) < 8: 
        print("Password is too short, it should contain at least 8 characters")
        return False 
    elif not re.search("[a-z]", password): 
        print("Password should contain at least one lowercase letter")
        return False 
    elif not re.search("[A-Z]", password): 
        print("Password should contain at least one uppercase letter")
        return False 
    elif not re.search("[0-9]", password): 
        print("Password should contain at least one number")
        return False 
    elif not re.search("[!@#$%^&*(){}<>:;,._+=-]", password): 
        print("Password should contain at least one special character")
        return False 
    else: 
        return True