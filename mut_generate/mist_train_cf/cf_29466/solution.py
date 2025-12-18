"""
QUESTION:
Create a function `extract_domains(emails: List[str]) -> List[str]` that takes a list of valid email addresses as input and returns a list of unique domain names. The domain name of an email address is the part that comes after the "@" symbol. Assume the input list is non-empty.
"""

from typing import List

def extract_domains(emails: List[str]) -> List[str]:
    return list(set(email.split('@')[-1] for email in emails))