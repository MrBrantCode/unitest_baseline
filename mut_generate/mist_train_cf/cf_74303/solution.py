"""
QUESTION:
Create a function `match_domains(email)` that identifies .edu, .gov, and international domain (non .com TLDs) email addresses while excluding subdomains and parent domains attached to the specified TLDs. The function should be efficient in distinguishing between valid and invalid email addresses with the mentioned endings. Note that this function only checks for the correct TLD endings and does not confirm the exact validity of the email address as per protocols.
"""

import re

def match_domains(email):
    pattern = r'^[a-zA-Z0-9_\-]+@[a-z0-9\-]+\.(?:edu|gov|[a-z]{2,}(?<!com))$'
    return re.match(pattern, email) != None