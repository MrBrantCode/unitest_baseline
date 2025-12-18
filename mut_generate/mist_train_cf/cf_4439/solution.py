"""
QUESTION:
Write a function named `calculate_total_length` that takes a list of email addresses as input, extracts the username and domain name from each email address, and returns the total number of characters in the username and domain name combined for all valid email addresses. The function should ignore email addresses with usernames shorter than 3 characters or domain names with less than 2 characters after the dot. The input list can have between 1 and 100 email addresses, each with a valid format and a length between 5 and 50 characters. The function should have a time complexity of O(n), where n is the number of email addresses in the list.
"""

def calculate_total_length(emails):
    total_length = 0

    for email in emails:
        username, domain = email.split('@')

        if len(username) >= 3 and len(domain.split('.')[-1]) >= 2:
            total_length += len(username) + len(domain)

    return total_length