"""
QUESTION:
Develop a function `extract_emails_categorize_domains(text_list)` that takes a list of strings as input and returns a dictionary where the keys are email domains and the values are lists of corresponding email addresses. The function should use regular expressions to extract email addresses from the input strings, handle exceptions where no valid email addresses are found, and support different email formats including subdomains.
"""

import re

def extract_emails_categorize_domains(text_list):
    # Regular expression pattern for matching email addresses
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Initialize empty dictionary to store emails categorized by domains
    email_dict = {}

    # Iterate over text list
    for text in text_list:
        # Use regex to find all emails in text element
        emails = pattern.findall(text)
        # If no emails are found, continue to next element
        if not emails:
            continue

        # Iterate over found emails
        for email in emails:
            # Extract domain from email
            domain = email.split('@')[-1]

            # If domain is not in dict, add it and initialize as empty list
            if domain not in email_dict:
                email_dict[domain] = []
            
            # Append email to domain list in dict
            email_dict[domain].append(email)

    return email_dict