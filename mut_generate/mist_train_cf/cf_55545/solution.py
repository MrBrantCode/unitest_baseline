"""
QUESTION:
Create a function `validate_emails(emails)` that takes a list of email addresses and returns two separate lists: one for valid email addresses and one for invalid email addresses. The function should use a regular expression to match email addresses, considering both local and internationalized domain names. Note that the regular expression should work well on most commonly used email formats, but may not confirm to all RFC rules.
"""

import re

def validate_emails(emails):
    # Regular expression based on commonly used email formats, does not confirm to all RFC rules
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    valid_emails = []
    invalid_emails = []
    
    for email in emails:
        if re.search(regex,email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
            
    return valid_emails, invalid_emails