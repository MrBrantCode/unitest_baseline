"""
QUESTION:
Implement a function `validateCredentials(username, password)` that takes a username and a password as input, replaces placeholders "${PT_username}" in the username and "${PT_password}" in the password with empty strings, then checks the credentials based on the following criteria: 
- The username is not empty and contains at least one alphanumeric character.
- The password is not empty, has a minimum length of 8 characters, and includes at least one uppercase letter, one lowercase letter, one digit, and one special character. 
Return True if the credentials are valid, False otherwise.
"""

import re

def validateCredentials(username, password):
    actual_username = username.replace("${PT_username}", "")
    actual_password = password.replace("${PT_password}", "")

    if actual_username and any(c.isalnum() for c in actual_username):
        if actual_password and len(actual_password) >= 8 and re.search(r'[A-Z]', actual_password) and re.search(r'[a-z]', actual_password) and re.search(r'\d', actual_password) and re.search(r'[^A-Za-z0-9]', actual_password):
            return True
    return False