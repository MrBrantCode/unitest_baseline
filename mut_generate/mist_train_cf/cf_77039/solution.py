"""
QUESTION:
Write a function `validate_emails(email_list)` that takes a list of email addresses and returns a list of email addresses that do not meet the validation criteria. The validation criteria are as follows:

- The email address should start with a series of alphanumeric characters and may include periods (.) or underscores (_).
- The series of alphanumeric characters should be followed by an '@' symbol.
- After '@' a series of alphanumeric characters representing the domain name is expected. This section can include hyphens (-) and period (.) but no other special characters are allowed here.
- The domain name should be followed by a top-level domain which begins with a period (.) and consists of at least two and no more than six alphabetic characters.
- The email address should not exceed 254 characters in length.
"""

import re

def validate_emails(email_list):
    regex_pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"
    invalid_emails = [email for email in email_list if not re.match(regex_pattern, email) or len(email) > 254]
    return invalid_emails