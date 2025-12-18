"""
QUESTION:
Write a function `extract_emails` that takes a list of text strings as input and returns a list of extracted email addresses. The function should use a regex pattern to identify email addresses in the text strings. The email pattern should match standard email addresses with alphanumeric characters, '.', '_', '%', '+', '-', '@', and a domain with two to three alphabetic characters after the final '.'. The function should return all email addresses found in the input text strings.
"""

import re

def extract_emails(text_list):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'
    emails = []

    for text in text_list:
        emails.extend(re.findall(email_pattern, text))
        
    return emails