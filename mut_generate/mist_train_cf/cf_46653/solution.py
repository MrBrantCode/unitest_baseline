"""
QUESTION:
Write a function called `verify_and_categorize` that takes a list of email addresses as input, verifies the validity of each email address using a regular expression, categorizes them based on their domain, and counts the occurrences of each domain. The function should handle multiple email addresses and return a dictionary where the keys are the domains and the values are the corresponding counts. If an email address is invalid, print an error message.
"""

import re
from collections import Counter

def verify_and_categorize(emails):
    """
    Verifies the validity of each email address using a regular expression, 
    categorizes them based on their domain, and counts the occurrences of each domain.

    Args:
        emails (list): A list of email addresses.

    Returns:
        dict: A dictionary where the keys are the domains and the values are the corresponding counts.
    """
    # Regular expression pattern for email verification
    pattern = r'[\w\.-]+@[\w\.-]+'
    email_counter = Counter()
    for email in emails:
        # If the email matches the pattern, it is valid
        if re.match(pattern, email):
            # Split the email at the '@' symbol and take the domain
            domain = email.split('@')[1]
            email_counter[domain] += 1
        else:
            print(f"Invalid email: {email}")
    return dict(email_counter)