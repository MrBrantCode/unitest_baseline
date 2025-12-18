"""
QUESTION:
Create a function named `find_edu_gov_emails` that takes a string as input and returns a list of strings representing the domain extensions ('edu' or 'gov') found in email addresses within the input string. The function should use a regular expression to match typical email address syntax, specifically targeting .edu and .gov domain extensions.
"""

import re

def find_edu_gov_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+(edu|gov)\b'
    return re.findall(pattern, text)