"""
QUESTION:
Create a function called `group_emails` that takes a list of email addresses as input and returns a dictionary. The function should group the email addresses by their domain, ignoring case sensitivity, and exclude any invalid email addresses. The output dictionary should be sorted in ascending order by domain name and include the count of unique email addresses for each domain and a list of the unique email addresses. Each email address in the list should only be counted once.
"""

import re

def group_emails(emails):
    # Dictionary to store the grouped email addresses
    grouped_emails = {}
    
    # Regular expression pattern to validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Iterate over each email address
    for email in emails:
        # Ignore case sensitivity
        domain = email.split('@')[1].lower()
        
        # Validate email format
        if re.match(email_pattern, email):
            # If the domain is not already in the grouped_emails dictionary, add it
            if domain not in grouped_emails:
                grouped_emails[domain] = {
                    'count': 1,
                    'emails': [email]
                }
            else:
                # Check if the email already exists before adding it
                if email not in grouped_emails[domain]['emails']:
                    grouped_emails[domain]['count'] += 1
                    grouped_emails[domain]['emails'].append(email)
    
    # Sort the grouped emails by domain names in ascending order
    sorted_grouped_emails = {k: v for k, v in sorted(grouped_emails.items(), key=lambda item: item[0])}
    
    return sorted_grouped_emails