"""
QUESTION:
Create a function `validate_email(email)` that takes a string as input, representing an email address, and returns a boolean or prints validation feedback. The function should use a regular expression to validate the email format and check if the domain is in a predefined list of allowed domains. The regular expression should account for case sensitivity, presence of sub-domains, and allow for common special characters used in emails. The list of allowed domains is `allowed_domains = ["gmail.com", "yahoo.com", "hotmail.com"]`.
"""

import re

# List of allowed domains
allowed_domains = ["gmail.com", "yahoo.com", "hotmail.com"]

# Regular Expression pattern for email validation
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def validate_email(email):
    # Check if the email matches the pattern
    if re.match(pattern, email):
        domain = email.split('@')[1].lower() #split the email at the @ to get the domain

        # Check if the domain is in the list of allowed domains
        if domain in allowed_domains:
            return True
        else:
            return False
    else:
        return False