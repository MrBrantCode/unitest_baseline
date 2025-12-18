"""
QUESTION:
Write a function called `validate_input` that takes two parameters: `username` and `password`. The function should return `True` if both the username and password meet the following requirements: 

1. The username must be at least 6 characters long and contain only lowercase letters.
2. The password must be at least 12 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g. !@#$%^&*).
3. The username and password must not be the same.
4. The password must not contain the username as a substring.

If any of the requirements are not met, the function should return `False` and provide an error message to guide the user.
"""

def validate_input(username, password):
    # Requirement 1: The username must be at least 6 characters long and contain only lowercase letters.
    if len(username) < 6 or not username.islower():
        print("Username must be at least 6 characters long and contain only lowercase letters.")
        return False
    
    # Requirement 2: The password must be at least 12 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
    if len(password) < 12 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password) or not any(char in '!@#$%^&*' for char in password):
        print("Password must be at least 12 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return False
    
    # Requirement 3: The username and password must not be the same.
    if username == password:
        print("Username and password cannot be the same.")
        return False
    
    # Requirement 4: The password must not contain the username as a substring.
    if username in password:
        print("Password must not contain the username as a substring.")
        return False
    
    # All requirements are met
    return True