"""
QUESTION:
Write a function `extract_contacts(text)` that takes a string `text` as input and returns a dictionary containing email addresses as keys and corresponding phone numbers (if present) as values. The function should extract email addresses with subdomains and only include addresses belonging to the 'example.com' domain. It should also remove any duplicate email addresses from the results. Phone numbers are assumed to be in the format XXX-XXX-XXXX.
"""

import re

def extract_contacts(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    emails = list(set(emails))
    domain = 'example.com'
    emails = [email for email in emails if email.endswith(domain)]

    contacts = {}
    for email in emails:
        for phone in phones:
            if email in text and phone in text:
                contacts[email] = phone

    return contacts