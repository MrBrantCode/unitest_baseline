"""
QUESTION:
Compose a function `replace_emails` that takes a string input and uses regular expressions to identify all occurrences of email addresses within the string, replacing them with the string "EMAIL".
"""

import re

def replace_emails(s):
    # Regular Expression pattern to find emails
    pattern = r'[\w\.-]+@[\w\.-]+'
    
    # replace emails with "EMAIL"
    result = re.sub(pattern, 'EMAIL', s)
    
    return result