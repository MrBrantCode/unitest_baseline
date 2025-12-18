"""
QUESTION:
Write a function `process_email_addresses` that takes a list of email addresses as input and returns a dictionary where the keys are the domain names and the values are lists of usernames. The function should handle both valid and invalid email addresses. 

For valid email addresses, the domain name should be used as the key, and the corresponding username should be added to the list of values. For invalid email addresses without domain names, the email address itself should be used as the key, and an empty list should be used as the value. If multiple email addresses have the same domain name, their usernames should be combined into a single list.
"""

from typing import List, Dict
import re

def process_email_addresses(emails: List[str]) -> Dict[str, List[str]]:
    email_dict = {}
    for email in emails:
        match = re.match(r'^([\w.-]+)@([\w.-]+)$', email)
        if match:
            username, domain = match.groups()
            email_dict.setdefault(domain, []).append(username)
        else:
            email_dict.setdefault(email, [])
    return email_dict