"""
QUESTION:
Create a function named `parse_email` that takes an email address as input and returns a dictionary containing the validity of the email, the username, domain, top-level domain (TLD), and any subdomains. The function should use regular expressions for validation and parsing, and should not rely on any built-in functions or libraries for verification or parsing of the email address.
"""

import re

def parse_email(email):
    email_regex = (r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    result = re.search(email_regex, email)
    if result:
        valid = True
        username, domain = email.split('@')
        elements = domain.split('.')
        tld = elements[-1]
        subdomains = elements[0:-1]
        subdomains = '.'.join(subdomains)
    else:
        valid = False
        username = domain = tld = subdomains = None

    return {
        "valid": valid,
        "username": username,
        "domain": domain,
        "tld": tld,
        "subdomains": subdomains
    }