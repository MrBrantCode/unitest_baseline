"""
QUESTION:
Write a function `preprocess_email(email_list)` that takes a list of email addresses as input, extracts the domain component from each email address, sorts the domains based on their frequency of occurrence in descending order, and then by lexicographical order in case of a tie. The function should handle potential irregularities such as missing domains, local parts, or @ symbols, excluding invalid email formats from the final list. The function should be case-insensitive, treating "Example.com" and "example.com" as the same.
"""

import re
from collections import Counter

def preprocess_email(email_list):
    # Regular Expression to validate the email
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    # list to store the domain component of email addresses
    domain_list = []

    for email in email_list:
        # validate email
        if re.match(email_regex, email):
            # If valid, get the domain component
            domain = email.split("@")[1].lower()
            domain_list.append(domain)

    # Get the frequency of each domain
    freq = Counter(domain_list)

    # Sort the domains based on their frequency and lexicographical order
    sorted_domains = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_domains