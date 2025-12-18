"""
QUESTION:
Write a function called `is_valid_password` that takes a password as input and returns a boolean value indicating whether the password is valid or not. The password is valid if it meets the following conditions: 
- It has a length of at least 12 characters.
- It contains at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, ^, &, *).
- It does not have any consecutive characters that are the same, in ascending or descending alphabetical order, or in ascending or descending numerical order.
The function should handle cases where the input password is None or an empty string, and return False for these cases. Do not use built-in functions or regular expressions.
"""

def is_valid_password(password):
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