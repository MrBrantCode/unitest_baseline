"""
QUESTION:
Create a function called `is_valid_email` that takes a string as input and returns `True` if the string can be used as a valid e-mail address and `False` otherwise. The function should follow these rules:
- The string should be split into two parts at the '@' symbol.
- The first part (username) should contain only alphanumeric characters, periods ('.'), underscores ('_'), and hyphens ('-').
- The second part (domain) should contain only alphanumeric characters and periods ('.').
- The domain should have at least one period ('.').
- The domain should have at least two characters after the last period ('.').
- The domain should not start or end with a period ('.').
- The username should not start or end with a period ('.'), hyphen ('-'), or underscore ('_').
- The username should not contain consecutive periods ('..'), hyphens ('--'), or underscores ('__').
"""

import re

def is_valid_email(string):
    parts = string.split('@')
    if len(parts) != 2:
        return False

    username = parts[0]
    domain = parts[1]

    if not re.match(r'^[\w.-]+$', username):
        return False

    if not re.match(r'^[a-zA-Z0-9.]+$', domain):
        return False

    if '.' not in domain:
        return False

    last_period_index = domain.rfind('.')
    if len(domain) - last_period_index < 3:
        return False

    if domain.startswith('.') or domain.endswith('.'):
        return False

    if username.startswith('.') or username.endswith('.'):
        return False

    if '..' in username:
        return False

    if username.startswith('-') or username.endswith('-'):
        return False

    if '--' in username:
        return False

    if username.startswith('_') or username.endswith('_'):
        return False

    if '__' in username:
        return False

    return True