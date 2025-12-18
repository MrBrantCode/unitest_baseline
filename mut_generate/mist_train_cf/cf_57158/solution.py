"""
QUESTION:
Create a function named `validate_registration` that takes in four parameters: `username`, `email`, `password`, and `confirm_password`. The function should validate these parameters according to the following rules:

- The `username` should be between 5 and 20 characters long.
- The `email` should be in the standard email address format.
- The `password` should be at least 8 characters long and contain a combination of at least one uppercase letter, one lowercase letter, one number, and one special character.
- The `confirm_password` should match the `password`.

If any of these validation steps fail, the function should return an error message indicating the specific validation failure. If all validation steps pass, the function should return a success message. The function should also handle cases where some or all of the parameters are missing, returning an error message if any parameter is not provided.
"""

import re

def validate_registration(username=None, email=None, password=None, confirm_password=None):
    if not username:
        return "Username is required."
    if len(username) < 5 or len(username) > 20:
        return "Username should have between 5 and 20 characters."
    
    if not email:
        return "Email is required."
    email_pattern = r'[^@]+@[^@]+\.[^@]+'
    if not re.match(email_pattern, email):
        return "Email format is incorrect."
    
    if not password:
        return "Password is required."
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not re.match(password_pattern, password):
        return "Password should have at least 8 characters, one uppercase letter, one lowercase letter, one number and one special character."
    
    if not confirm_password:
        return "Confirm password is required."
    if password != confirm_password:
        return "Password and confirm password do not match."
    
    return "New user has been registered successfully."