"""
QUESTION:
Create a function `is_valid_email(email)` that checks if an email address is valid based on the following conditions: 
- contains an "@" symbol
- contains a "."
- has at least 6 characters
- starts with a letter
- does not contain any special characters other than "." and "@"
- does not have consecutive "." or "@"
- does not have a "." immediately after the "@"
- has at least one letter before the "@" symbol
- has at least two letters after the last "."
- does not start or end with a "." or "@"
The function should take an email address as input and return True if it is valid, and False otherwise. Do not use built-in libraries or regular expressions for this task.
"""

def is_valid_email(email):
    if len(email) < 6:
        return False
    if email[0] == '.' or email[0] == '@':
        return False
    if email[-1] == '.' or email[-1] == '@':
        return False
    if '@@' in email or '..' in email:
        return False
    if email.count('@') != 1 or email.count('.') < 1:
        return False
    
    atIndex = email.find('@')
    dotIndex = email.rfind('.')
    
    if atIndex < 1 or dotIndex < atIndex + 2 or dotIndex == -1 or len(email) - dotIndex < 3:
        return False
    
    for char in email:
        if not (char.isalpha() or char == '.' or char == '@'):
            return False
    
    return True