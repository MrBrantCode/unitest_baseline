"""
QUESTION:
Create a Python function named `extract_emails` that takes a string `input_string` and extracts all the email addresses in the format `name@server` from the input. The function should then create a JSON object containing the extracted email addresses and the number of times each email address appears in the input.
"""

import re
import json
def extract_emails(input_string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, input_string)
    email_dict = {}
    for email in emails:
        if email in email_dict:
            email_dict[email] += 1
        else:
            email_dict[email] = 1
    email_json = json.dumps(email_dict)
    return email_json