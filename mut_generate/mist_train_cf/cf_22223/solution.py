"""
QUESTION:
Create a function `is_valid_password(password)` that checks if the given string can be used as a valid password according to the following requirements:
 
- The password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character (!@#$%^&*()-_=+[]{}|;':",./<>?`~).
- The password must have a length between 8 and 20 characters (inclusive).
- The password must not start or end with a whitespace character.
- The password must not contain consecutive identical characters.

Return True if all conditions are satisfied, indicating that the string can be used as a valid password, and False otherwise.
"""

def is_valid_password(password):
    # Check length
    if len(password) < 8 or len(password) > 20:
        return False
    
    # Check for lowercase, uppercase, digit, and special character
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
        elif char in "!@#$%^&*()-_=+[]{}|;':\",./<>?`~":
            has_special = True
            
    if not has_lowercase or not has_uppercase or not has_digit or not has_special:
        return False
    
    # Check for leading or trailing whitespace
    if password[0].isspace() or password[-1].isspace():
        return False
    
    # Check for consecutive identical characters
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return False
    
    # All conditions satisfied
    return True