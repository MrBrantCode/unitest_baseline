"""
QUESTION:
Design a function `is_valid_password(password)` that determines whether a given password is valid based on the following conditions: 
- The password length must be between 8 and 15 characters.
- The password must contain at least one digit.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one special character (!, #, $, %, &, ', (, ), *, +, -, ., /, :, ;, <, =, >, ?, @, [, \, ], ^, _, `, {, |, }, or ~).
"""

import re

def is_valid_password(password):
    #check password length
    if len(password) < 8 or len(password) > 15:
        return False

    #check for at least one digit
    if re.search(r"[0-9]",password) is None:
        return False
    
    #check for at least one uppercase letter
    if re.search(r"[A-Z]",password) is None:
        return False
    
    #check for at least one lowercase letter
    if re.search(r"[a-z]",password) is None:
        return False
    
    #check for at least one special character  
    if re.search(r"[!#$%&'()*+,-./:;<=>?@[\] ^_`{|}~]",password) is None:
        return False

    #if all conditions are met, password is valid
    return True