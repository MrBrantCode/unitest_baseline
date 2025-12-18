"""
QUESTION:
Write a function named `find_email_addresses` that takes a list of strings as input and returns a list of email addresses found in the strings. The email addresses should be in the format of one or more alphanumeric characters or special characters (dot, hyphen), followed by '@', followed by one or more alphanumeric characters or special characters (dot, hyphen), and ending with a domain extension (one or more alphanumeric characters). The function should be case-sensitive and should not validate the existence of the email addresses.
"""

import re

def find_email_addresses(text_list):
    """
    This function takes a list of strings as input and returns a list of email addresses found in the strings.
    
    Args:
        text_list (list): A list of strings that may contain email addresses.
    
    Returns:
        list: A list of email addresses found in the input strings.
    """

    # Regular expression pattern to match email addresses
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    # Initialize an empty list to store the email addresses
    emails = []

    # Loop through each string in the list
    for text in text_list:
        # Find all matches of the pattern in the current string
        matches = re.findall(pattern, text)
        # Extend the email list with the matches
        emails.extend(matches)

    # Return the list of email addresses
    return emails