"""
QUESTION:
Create a function named `extract_emails` that takes a string input and extracts all the email addresses in the format `name@server`. The function should return a JSON object containing the extracted email addresses and the number of times each email address appears in the input. The email address format should be `name@server` where `name` can contain letters (both uppercase and lowercase), numbers, dot (.), hyphen (-), underscore (_), percent (%), and plus sign (+), and `server` can contain letters (both uppercase and lowercase), numbers, dot (.), and hyphen (-). The function should be case-sensitive and consider "John@example.com" and "john@example.com" as two different email addresses.
"""

import re
import json

def extract_emails(input_string):
    # Define a regular expression pattern for email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Find all email addresses in the input string
    emails = re.findall(pattern, input_string)
    # Create a dictionary to store the email addresses and their frequencies
    email_dict = {}
    for email in emails:
        if email in email_dict:
            email_dict[email] += 1
        else:
            email_dict[email] = 1
    # Convert the dictionary to a JSON object
    email_json = json.dumps(email_dict)
    return email_json