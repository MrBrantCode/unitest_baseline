"""
QUESTION:
Create a function named `is_valid_email` that takes a string and checks if it's a valid email or not. The string must follow the format of "username@domain.com", where the username can only contain lowercase letters, numbers, periods, underscores, and hyphens, and must start and end with a letter or a number. The domain must consist of at least two levels, separated by periods, and each level can only contain lowercase letters and hyphens.
"""

import re

def is_valid_email(email):
    username, domain = email.split('@')
    
    if not re.match(r'^[a-z0-9][a-z0-9_.-]*[a-z0-9]$', username):
        return False
    
    if not re.match(r'^[a-z0-9-]+(\.[a-z0-9-]+)+$', domain):
        return False
    
    return True