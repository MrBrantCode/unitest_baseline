"""
QUESTION:
Develop a function named `extract_emails` that takes a list of text strings as input and returns a list of extracted email addresses. The function should use a regex pattern to identify valid email addresses, considering variations like .co, .gov, .edu, and optional country codes (.uk, .in, etc.). The function should ignore any email addresses where the username starts or ends with a special character (dot, underscore, or hyphen).
"""

import re

def extract_emails(text_list):
    email_list = []
    regex_pattern = r"(?:[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    
    for text in text_list:
        emails = re.findall(regex_pattern, text)
        for email in emails:
            if not re.match(r".*[\._-]$|^[._-].*", email):
                email_list.append(email)
    
    return email_list