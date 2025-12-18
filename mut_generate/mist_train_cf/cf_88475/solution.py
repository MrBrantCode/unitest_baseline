"""
QUESTION:
Write a function `calculate_total_length` that takes a list of email addresses as input and returns the total number of characters in the username and domain name combined for all valid email addresses. The list can have a minimum of 1 and a maximum of 100 email addresses. Each email address must have a valid format with a minimum length of 5 characters and a maximum length of 50 characters. The username must consist of alphanumeric characters only and be at least 3 characters long. The domain name must be a valid domain with at least 2 characters after the dot. The function should have a time complexity of O(n), where n is the number of email addresses in the list.
"""

def calculate_total_length(emails):
    total_length = 0

    for email in emails:
        username, domain = email.split('@')

        if len(username) >= 3 and len(domain) >= 4:
            total_length += len(username) + len(domain)

    return total_length