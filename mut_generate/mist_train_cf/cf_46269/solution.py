"""
QUESTION:
Create a function `classify_emails_by_domain` that uses regex to extract email addresses from a given string and categorize them based on their domain extensions. The function should handle case-sensitive and multiple email addresses per domain. The output should be a dictionary where the keys are the domain names and the values are lists of usernames.
"""

import re

def classify_emails_by_domain(content):
    """
    Uses regex to extract email addresses from a given string and categorize them based on their domain extensions.

    Args:
    content (str): A string containing email addresses.

    Returns:
    dict: A dictionary where the keys are the domain names and the values are lists of usernames.
    """
    # Here's the regex expression - it captures "word@word.domain"
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Using the regex findall method
    emails = re.findall(regex, content)

    # Use dictionary to classify emails based on domain
    email_dict = {}
    for email in emails:
        username, domain = email.split('@')
        if domain not in email_dict:
            email_dict[domain] = [username]
        else:
            email_dict[domain].append(username)

    return email_dict