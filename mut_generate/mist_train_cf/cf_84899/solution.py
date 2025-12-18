"""
QUESTION:
Write a function `extract_domain(email)` that takes an email address as input and returns the domain component. The function should handle subdomains and unexpected email formats, returning an error message in such cases. The function should be able to differentiate between correct and incorrect email formats.
"""

import re

def extract_domain(email):
    """Extracts the domain from the given email address"""
    try: 
        # regex for finding domain names, got from stackoverflow
        match = re.search(r'@[\w.]+', email)

        if match is not None:
            domain = match.group().strip('@')
            return domain
        else:
            return "Invalid email format"

    except Exception as e:
        return str(e)