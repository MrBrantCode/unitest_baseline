"""
QUESTION:
Create a function `sort_emails(emails)` that takes a list of email addresses as input. The function should sort the list based on two criteria: the total character count of the email address, and the count of unique characters in the local part (before '@'). Emails with the same total character count should be sorted by the count of unique characters in ascending order. The function should also discard any invalid email addresses from the sorting.
"""

import re

def sort_emails(emails):
    """ Sorts emails based on total character count and then by count of unique characters in the local part """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    valid_emails = [email for email in emails if re.match(regex, email)] # filter out invalid emails
    
    # sort by total character count and then by count of unique characters in the local part
    valid_emails.sort(key=lambda x: (len(x), len(set(x.split('@')[0]))))
    
    return valid_emails