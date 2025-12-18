"""
QUESTION:
Write a function named `process_emails` that takes a list of tuples, where each tuple contains an email address, a full name, and an age. The function should return a dictionary where the keys are valid email addresses and the values are tuples containing the full name, age as an integer, and the length of the username part of the email address. A valid email address is one that matches the format [username]@[domain].[extension]. Only include email addresses in the dictionary if the age is 40 or older. The function should be able to handle a list of up to 1 million elements with a time complexity of O(n) or better.
"""

import re

def process_emails(emails):
    email_dict = {}
    pattern = r'^([\w\.-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z\.]{2,})$'
    for email, name, age in emails:
        match = re.match(pattern, email)
        if match and int(age) >= 40:
            username = match.group(1)
            email_dict[email] = (name, int(age), len(username))
    return email_dict