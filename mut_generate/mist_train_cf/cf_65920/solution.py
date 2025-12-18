"""
QUESTION:
Write a Python function named `extract_info` that takes a string as input and returns a dictionary containing the extracted emails, phone numbers, and URLs. The function should use regular expressions to match different formats for emails, phone numbers, and URLs. The email pattern should support alphanumeric characters and special characters like `_ % + - .`. The phone number pattern should match different formats such as `123-456-7890`, `123.456.7890`, `(123) 456-7890`, and `+1-(800)-123-4567`. The URL pattern should match `http`, `https`, and `ftp` protocols.
"""

import re

def extract_info(text):
    """
    Extracts emails, phone numbers, and URLs from the given text.

    Args:
    text (str): The text to extract information from.

    Returns:
    dict: A dictionary containing the extracted emails, phone numbers, and URLs.
    """

    # Email Pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Phone Number Pattern
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\+\d{2}-\(\d{3}\)-\d{3}-\d{4}'

    # URL pattern
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|ftp://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Extracting
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    urls = re.findall(url_pattern, text)

    # Return the extracted information as a dictionary
    return {
        "emails": emails,
        "phones": phones,
        "urls": urls
    }