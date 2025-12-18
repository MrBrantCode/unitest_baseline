"""
QUESTION:
Write a function `validate_password(password)` that checks the validity of a given password. The password is valid if it meets the following conditions: 
- It contains at least one lowercase letter, one uppercase letter, one number, and one special character.
- It is at least 8 characters long.
- It does not contain any consecutive repeating characters.
- It is not a common or easily guessable password (compare it to a predefined list of common passwords). 
The function should return a boolean value indicating whether the password is valid or not.
"""

def validate_password(password):
    # Check password length
    if len(password) < 8:
        return False
    
    # Check if password contains at least one lowercase letter, one uppercase letter, one number, and one special character
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    
    if not has_lower or not has_upper or not has_digit or not has_special:
        return False
    
    # Check if password contains consecutive repeating characters
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            return False
    
    # Check if password is a common or easily guessable password
    common_passwords = ['password', '12345678', 'qwerty', 'abc123']  # Add more common passwords as needed
    if password in common_passwords:
        return False
    
    # Password is valid if it passes all checks
    return True