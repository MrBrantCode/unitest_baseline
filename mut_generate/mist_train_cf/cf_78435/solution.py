"""
QUESTION:
Create a function `validate_emails(email_list, valid_domains=None)` that validates a list of email addresses according to standard email specifications. The function should use a regex pattern to check for valid email formats and, if provided, filter the results to only include emails from a predefined list of acceptable domains. The function should return a list of valid email addresses.
"""

import re 

def validate_emails(email_list, valid_domains=None):
    # Regex pattern for a standard email
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    
    # Validating emails 
    valid_emails = [email for email in email_list if re.match(email_pattern, email)]
    
    # If a list of valid domains is provided, then further validate the valid emails
    if valid_domains:
        valid_emails = [email for email in valid_emails
                        if any(email.endswith(f'@{dom}') for dom in valid_domains)]
    
    return valid_emails