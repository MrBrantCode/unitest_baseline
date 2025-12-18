"""
QUESTION:
Develop a function `find_emails` that identifies multiple email addresses from a given text document using Regular Expressions. The function should be able to account for variations of email addresses with different domain extensions (e.g., '.com', '.net', '.org', '.edu', etc.) or country-specific codes (e.g., '.co.uk', '.com.au', etc.). The function should return all identified email addresses in an organized list format. The function should validate the correctness of each address according to standard email formatting rules.
"""

import re

def find_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(pattern, text)
    return emails