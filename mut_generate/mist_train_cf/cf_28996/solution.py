"""
QUESTION:
Write a function `extract_email` that takes a dictionary `data` as input and returns the email address extracted from the dictionary in a standardized format. The email address is stored in the "email" key and may contain angle brackets that need to be removed.
"""

import re

def extract_email(data):
    """Extracts and formats the email address from the input dictionary."""
    email = data["email"]
    formatted_email = re.sub(r'<|>', '', email)  # Removing '<' and '>' from the email
    return formatted_email