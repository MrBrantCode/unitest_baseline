"""
QUESTION:
Create a function `check_email(email)` that takes an email address as input and returns a string indicating whether the email syntax is valid and if it contains any common phishing indicators in the domain part. The function should use a regular expression to check the email syntax and a predefined list of common misspelled popular domains to identify potential phishing attempts.
"""

import re

def check_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.search(pattern, email):
        return "Invalid email syntax."

    domain = email.split('@')[1]
    
    # Common misspelled popular domains
    phishing_domains = ["goggle.com", "gooogle.com", "yaho.com", "hormail.com", 
                        "hotmall.com", "hotmial.com", "hotmali.com", "hotmai.com"]
    
    for phish_domain in phishing_domains:
        if phish_domain in domain:
            return f"Potential phishing attempt, detected commonly misspelled domain: {phish_domain}."

    return "Email appears to be valid and free from common phishing indicators."