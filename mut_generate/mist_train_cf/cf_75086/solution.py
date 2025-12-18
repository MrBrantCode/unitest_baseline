"""
QUESTION:
Write a function `extract_emails(text_list)` that develops a regular expression pattern to identify and extract email addresses from a list of text strings. The function should correctly identify emails even if they are presented in different formats, or with varying degrees of complexity such as emails with subdomains. It should account for potential erroneous strings and handle any occurring errors gracefully. The function should return a list of extracted email addresses. The input `text_list` is a list of strings, and the function should work correctly for any valid input list.
"""

import re

def extract_emails(text_list):
    try:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_list = []

        for text in text_list:
            emails = re.findall(pattern, text)
            email_list.extend(emails)
        
        return email_list

    except Exception as e:
        print(f"An error occurred: {str(e)}")