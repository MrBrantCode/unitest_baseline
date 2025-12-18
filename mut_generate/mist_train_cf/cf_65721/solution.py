"""
QUESTION:
Write a function `find_emails` that constructs a regex pattern to identify valid email addresses in a given text. The email should start with an alphabetic character, allow underscores and hyphens in the username part, have a domain consisting of any number of subdomains separated by a "." (dot), and end with a top-level domain being either .com, .net or .org.
"""

import re

def find_emails(text):
    pattern = r'\b[A-Za-z][A-Za-z0-9\_\-]*@[A-Za-z0-9\-]+\.(?:com|org|net)(?:\.[A-Za-z0-9]+)*'
    return re.findall(pattern, text)