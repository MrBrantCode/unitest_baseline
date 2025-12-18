"""
QUESTION:
Create a function `check_password_strength(password)` that tests the strength, reliability, and resilience to a dictionary attack of a given password. The function should check if the password meets the following requirements:

- The password length should be at least 8 characters long.
- The password should contain at least one special character.
- The password should contain at least one digit.
- The password should contain at least one uppercase letter.
- The password should contain at least one lowercase letter.
- The password should not be in a given list of common passwords.

The function should return a string indicating whether the password is strong or not. If the password does not meet any of the requirements, the function should return a string describing the issue. If the password is in the list of common passwords, the function should return a string indicating that the password is too common.
"""

import re

def check_password_strength(password, common_passwords):
    """
    Tests the strength, reliability, and resilience to a dictionary attack of a given password.
    
    Parameters:
    password (str): The password to be checked.
    common_passwords (list): A list of common passwords.
    
    Returns:
    str: A string indicating whether the password is strong or not.
    """
    
    # checking the length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long"
    
    # checking for special characters
    if not re.search("[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", password):
        return "Password should have at least one special character"
    
    # checking for digits
    if not re.search("[0-9]", password):
        return "Password should have at least one digit"
    
    # checking for uppercase
    if not re.search("[A-Z]", password):
        return "Password should have at least one uppercase letter"
    
    # checking for lowercase
    if not re.search("[a-z]", password):
        return "Password should have at least one lowercase letter"
    
    # checking for common passwords
    if password+'\n' in common_passwords:
        return "That password is too common. Choose a different password."
    
    return "Password seems strong."