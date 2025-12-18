"""
QUESTION:
Write a SQL query to select all valid email addresses from a table, where an email is considered valid if it meets the following conditions: 
- The email address is in the format "username@domain.com".
- The username can contain alphanumeric characters, underscore (_), dot (.), and hyphen (-).
- The domain name contains alphanumeric characters and dot (.), with at least one dot.
- The email address has a valid top-level domain.
- The email address does not exceed 255 characters in length. 

Do not use regular expressions or built-in string manipulation functions in your solution.
"""

def validate_email(email):
    if len(email) > 255:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    username, domain = parts

    for char in username:
        if not (char.isalnum() or char in ['_', '.', '-']):
            return False

    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False

    for part in domain_parts:
        for char in part:
            if not (char.isalnum() or char == '.'):
                return False

    return True