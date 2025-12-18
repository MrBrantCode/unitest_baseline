"""
QUESTION:
Create a function called `extract_copyright_email` that takes a code snippet as input. The function should extract the copyright information and the email address from the code snippet, denoted by `@copyright` and `@Email` respectively within a multi-line comment format, and return them in a structured format. The function should handle cases where the copyright and/or email information is not found in the code snippet.
"""

import re

def extract_copyright_email(code_snippet):
    copyright_pattern = r'@copyright \(C\) (\d{4} - \d{4}) (.+?)\n'
    email_pattern = r'@Email: (.+?)\n'
    
    copyright_match = re.search(copyright_pattern, code_snippet, re.IGNORECASE)
    email_match = re.search(email_pattern, code_snippet, re.IGNORECASE)
    
    if copyright_match and email_match:
        copyright_info = copyright_match.group(1) + ' ' + copyright_match.group(2)
        email = email_match.group(1)
        return {'copyright': copyright_info, 'email': email}
    else:
        return {'copyright': None, 'email': None}