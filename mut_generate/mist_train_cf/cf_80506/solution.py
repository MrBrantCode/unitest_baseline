"""
QUESTION:
Implement a function `extract_emails` that takes a string `content` as input and returns a list of all valid email addresses found in the string. The email addresses should be in the format `local-part@domain` and may contain special characters, including plus signs (+) and periods (.) in the local part, as well as sub-domains. Use regular expressions to validate and extract the email addresses. The function should correctly handle alphanumeric characters, hyphens, periods, numeric characters, and potential sub-domains during the validation process.
"""

import re

def extract_emails(content):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, content)
    return emails