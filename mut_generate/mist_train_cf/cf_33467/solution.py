"""
QUESTION:
Create a function `validate_registration(username, password, password_confirmation)` that validates user registration information. The function should return `True` if the registration information is valid and `False` otherwise. The validation rules are:
- The username must contain only alphanumeric characters and spaces.
- The password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
- The password and password confirmation must match.
"""

def entrance(username, password, password_confirmation):
    # Validate username
    if not username.replace(' ', '').isalnum():
        return False
    
    # Validate password
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    special_chars = set('!@#$%^&*()_+-=[]{}|;:,.<>?')
    if not any(char in special_chars for char in password):
        return False
    
    # Confirm password
    if password != password_confirmation:
        return False
    
    return True