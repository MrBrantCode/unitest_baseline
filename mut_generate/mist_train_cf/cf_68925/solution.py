"""
QUESTION:
Write a function `validate_emails(emails)` that takes a list of email addresses as input and returns a list of valid email addresses. The email addresses are valid if they meet the following conditions:

- The email address must start with a letter (a-z, A-Z).
- Special characters like underscores(_), periods(.), and hyphens(-) can occur after the first character only.
- The domain name may contain letters, numbers, and hyphens.
- The TLD (.com) must be specified clearly, and no other text should come after it.
"""

import re

def validate_emails(emails):
    pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9-]+\.(com)$"
    return [email for email in emails if re.search(pattern, email)]