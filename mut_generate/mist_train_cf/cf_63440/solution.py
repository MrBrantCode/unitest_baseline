"""
QUESTION:
Write a function `find_emails(text)` that retrieves all valid email addresses from a provided text, validates the addresses, and categorizes them into two lists: one for Gmail addresses and another for other email addresses. A valid email address must meet the following conditions:

- It contains one @ character.
- It contains at least one character before and after the @ character.
- It contains at least one '.' character after the @, and it must be after all other characters that are not '@' or '.'.
- The domain name (part of the email after the '.') should only contain alphabetic characters.

The function should return two lists: the first list containing Gmail addresses and the second list containing other email addresses.
"""

import re

def find_emails(text):
    # Regular expression pattern matching a valid e-mail address.
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matching email addresses in the text.
    emails = re.findall(pattern, text)

    # Empty lists to hold gmail and other email addresses.
    gmail_addresses = []
    other_addresses = []

    # Fill the gmail and other email address lists accordingly.
    for email in emails:
        if 'gmail.com' in email:
            gmail_addresses.append(email)
        else:
            other_addresses.append(email)

    return gmail_addresses, other_addresses