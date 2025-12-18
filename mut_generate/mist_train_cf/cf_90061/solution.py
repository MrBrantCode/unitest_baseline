"""
QUESTION:
Create a function named `is_valid_password` that checks if a given string can be used as a valid password. The password is valid if it meets the following requirements: 
- It contains at least one lowercase letter, one uppercase letter, one digit, and one special character (!@#$%^&*()-_=+[]{}|;':",./<>?`~).
- Its length is between 10 and 25 characters (inclusive).
- It does not start or end with a whitespace character.
- It does not contain any repeating consecutive characters of the same type (e.g., "aa" or "11").
- It does not contain any repeating consecutive characters of different types (e.g., "AbAb" or "12ab").
- If all conditions are met, return True; otherwise, return False.
"""

def is_valid_password(password):
    # Check the length of the password
    if len(password) < 10 or len(password) > 25:
        return False
    
    # Check if the password starts or ends with whitespace
    if password[0].isspace() or password[-1].isspace():
        return False
    
    # Check if the password contains at least one lowercase letter, one uppercase letter, one digit, and one special character
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in '!@#$%^&*()-_=+[]{}|;:\'",./<>?`~':
            has_special = True
    if not (has_lowercase and has_uppercase and has_digit and has_special):
        return False
    
    # Check for repeating consecutive characters of the same type
    for i in range(len(password) - 1):
        if password[i] == password[i+1] and (password[i].isalpha() or password[i].isdigit()):
            return False
    
    # Check for repeating consecutive characters of different types
    for i in range(len(password) - 3):
        if password[i] == password[i+2] and password[i+1] == password[i+3]:
            return False
    
    # All conditions are satisfied
    return True