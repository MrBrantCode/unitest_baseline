"""
QUESTION:
Create a function `process_emails` that takes a list of tuples containing email, name, and age as input. The function should validate each email and only include it in the output dictionary if it is in the correct format of [username]@[domain].[extension] and the age is 40 or older. The output dictionary should contain the email as the key and a tuple of name, age as an integer, and the length of the username as the value. The function should have a time complexity of O(n), where n is the number of elements in the input list.
"""

import re

def process_emails(emails):
    email_dict = {}
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z\.]{2,}$'
    for email, name, age in emails:
        if re.match(pattern, email):
            username = email.split('@')[0]
            if int(age) >= 40:
                email_dict[email] = (name, int(age), len(username))
    return email_dict