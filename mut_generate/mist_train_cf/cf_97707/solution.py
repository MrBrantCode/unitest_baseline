"""
QUESTION:
Write a function called `extract_contacts_from_html` that takes a string of HTML as input, extracts all phone numbers and email addresses using regular expressions, and returns them as two separate lists. The function should be able to handle different formats of phone numbers and email addresses. 

The phone number format may vary but it can be identified by the presence of 10 consecutive digits with possible delimiters such as '(', ')', '-', ' ', or '.'. 

The email address format is standard, consisting of alphanumeric characters, dots, and underscores before the '@' symbol and alphanumeric characters, dots, and underscores after the '@' symbol, followed by a dot and at least one more alphanumeric character.
"""

import re

def extract_contacts_from_html(html):
    # Define regex patterns for phone numbers and email addresses
    phone_pattern = re.compile(r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})')
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')

    # Extract phone numbers and email addresses
    phone_numbers = phone_pattern.findall(html)
    email_addresses = email_pattern.findall(html)
    
    return phone_numbers, email_addresses