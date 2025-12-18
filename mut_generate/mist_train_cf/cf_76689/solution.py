"""
QUESTION:
Create a function `validate_email(email)` that takes an email address as input and returns 'Valid email.' if it matches a specific pattern using regular expressions and has a domain from a predefined list of allowed domains ('example.com', 'test.com'). The function should return 'Invalid email.' otherwise. The allowed domains list should be defined within the function. The function should validate common email formats that require at least one character before the '@', then any number of characters, then a period, then at least two characters, and allow numbers, periods, percent signs, plus signs, dashes, and underscores.
"""

import re

def validate_email(email):
    email_domain = email.split('@')[-1]
    allowed_domains = ['example.com', 'test.com']

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pattern, email) and email_domain in allowed_domains:
        return 'Valid email.'
    else:
        return 'Invalid email.'