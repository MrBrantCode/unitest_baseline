"""
QUESTION:
Group email addresses by their domain. Create a function called `group_emails_by_domain` that takes a list of email addresses as input and returns a dictionary where the keys are the domains and the values are lists of email addresses belonging to each domain. Assume that the input list contains valid email addresses and the domain is the part after the "@" symbol.
"""

from collections import defaultdict

def group_emails_by_domain(emails):
    """
    This function groups email addresses by their domain.

    Args:
        emails (list): A list of email addresses.

    Returns:
        dict: A dictionary where the keys are the domains and the values are lists of email addresses belonging to each domain.
    """
    by_domain = defaultdict(list)

    for email in emails:
        domain = email.split("@")[-1]
        by_domain[domain].append(email)

    return dict(by_domain)