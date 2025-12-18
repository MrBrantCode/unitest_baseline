"""
QUESTION:
Write a Python function `test_email_regex` that uses a regular expression to validate email addresses. The function should compile a case-insensitive regex pattern that matches valid email addresses with the following characteristics: 
- The username can contain alphanumeric characters, dots, underscores, pluses, and hyphens.
- The domain name can contain alphanumeric characters, hyphens, and periods.
- The domain name must have at least one period.
The function should then test the regex pattern with both positive and negative test cases to ensure it correctly matches valid email addresses and rejects invalid ones.
"""

import re

def test_email_regex(email: str) -> bool:
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.IGNORECASE)
    return bool(email_regex.match(email))