"""
QUESTION:
Write a function `is_valid_password(password)` that takes a password as input and returns `True` if the password is valid and `False` otherwise. 

A password is considered valid if it meets the following criteria: 
- It contains at least 12 characters.
- It contains at least one uppercase letter.
- It contains at least one lowercase letter.
- It contains at least one digit.
- It contains at least one special character (!, @, #, $, %, ^, &, *).
- It does not contain any consecutive characters that are the same.
- It does not contain any consecutive characters that are in ascending or descending alphabetical order.
- It does not contain any consecutive characters that are in ascending or descending numerical order.

The function should also handle the case when the input password is `None` or an empty string, and return `False` in such cases.
"""

def entrance(password):
    if password is None or password == "":
        return False
    
    if len(password) < 12:
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    
    for i in range(len(password)):
        if i > 0:
            if password[i] == password[i-1]:
                return False
            
            if password[i].isalpha() and password[i-1].isalpha():
                if ord(password[i]) == ord(password[i-1]) + 1 or ord(password[i]) == ord(password[i-1]) - 1:
                    return False
            
            if password[i].isdigit() and password[i-1].isdigit():
                if int(password[i]) == int(password[i-1]) + 1 or int(password[i]) == int(password[i-1]) - 1:
                    return False
        
        if password[i].isupper():
            has_uppercase = True
        elif password[i].islower():
            has_lowercase = True
        elif password[i].isdigit():
            has_digit = True
        elif password[i] in "!@#$%^&*":
            has_special = True
    
    return has_uppercase and has_lowercase and has_digit and has_special