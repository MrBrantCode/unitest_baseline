"""
QUESTION:
Create a function named `validate_email` that takes an email address as a string and a set of valid domains as an optional argument (defaulting to `{"com", "edu", "org"}`), and returns a string indicating whether the email address is valid or not. The function should use regex to validate the email format, exclude blacklisted domains (e.g., "invalid.com", "blacklisted.com"), and only allow emails with the specified valid domains.
"""

import re

def validate_email(email, valid_domains={"com", "edu", "org"}):
    domain_blacklist = {"invalid.com", "blacklisted.com"}
    email_regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_regex, email):
        domain = email.split("@")[-1]
        if domain in domain_blacklist:
            return f"Error: The domain {domain} is blacklisted."
        elif domain.split(".")[-1] in valid_domains:
            return "The email is valid."
        else:
            return "Error: The email domain is not valid."
    else:
        return "Error: The email format is not valid."