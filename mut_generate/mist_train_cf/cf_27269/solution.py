"""
QUESTION:
Create a function named `extract_emails` that takes a string as input and returns a list of unique email addresses found within the input string in lexicographical order. A valid email address is defined as a string of the form "username@domain.com" where both the username and domain can contain letters, numbers, dots, and hyphens. The username cannot start or end with a dot or hyphen, and the domain must contain at least one dot. The function should ignore any invalid email addresses or duplicates.
"""

import re

def extract_emails(input_string):
    email_regex = r'\b[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, input_string)
    unique_emails = list(set(emails))
    unique_emails.sort()
    return unique_emails