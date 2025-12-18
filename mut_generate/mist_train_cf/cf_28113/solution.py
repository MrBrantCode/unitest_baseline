"""
QUESTION:
Create a function `countUniqueEmails(emails)` that takes a list of email addresses as input and returns the count of unique, formatted email addresses. 

The formatting process for each email address involves: 
- ignoring any characters after the '+' symbol in the local name, 
- removing all periods in the local name, 
- and concatenating the local name and domain name with '@'. 
Two email addresses are considered unique if they are the same after applying these formatting rules.
"""

from typing import List

def countUniqueEmails(emails: List[str]) -> int:
    unique_emails = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        unique_emails.add(local + '@' + domain)
    return len(unique_emails)