"""
QUESTION:
Create a function `find_illegal_characters(email_list)` that takes a list of email addresses as input and returns a list of indices where illegal characters are found in the usernames. The function should consider any character that is not a letter (both uppercase and lowercase), digit, or one of the special characters ".-_@" as an illegal character, and the index should be relative to the "@" symbol in each email address.
"""

def find_illegal_characters(email_list):
    illegal_indices = []
    for email in email_list:
        username, domain = email.split('@')
        for i, char in enumerate(username):
            if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-":
                illegal_indices.append(email.index('@') + i)
    return illegal_indices