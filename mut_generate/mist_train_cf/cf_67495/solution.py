"""
QUESTION:
Create a function `identify_email(email)` that takes a string email address as input and returns "Personal email" if it is from a personal email domain (gmail, yahoo, or hotmail), "Business email" if it is from any other domain, and "Invalid email" if the input string is not a valid email address. A valid email address consists of a local part (1-64 alphanumeric characters and symbols '.', '-', and '+') followed by '@' and a domain part (two subsections separated by a '.'), and it should match the specified format.
"""

import re

personal_regex = r"^[a-zA-Z0-9_.+-]+@(gmail|yahoo|hotmail)\.com$"
business_regex = r"^[a-zA-Z0-9_.+-]+@(?!(gmail|yahoo|hotmail)\.com)([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def identify_email(email):
    personal_match = re.match(personal_regex, email)
    business_match = re.match(business_regex, email)
    
    if personal_match:
        return "Personal email"
    elif business_match:
        return "Business email"
    else:
        return "Invalid email"