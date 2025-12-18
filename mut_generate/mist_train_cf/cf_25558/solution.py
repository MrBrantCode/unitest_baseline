"""
QUESTION:
Write a function to filter valid email addresses from a list of email addresses. A valid email address is defined as a string containing '@' followed by at least one character, followed by '.' and at least one character after the '.'.
"""

def filter_valid_emails(emails):
    def is_valid(email):
        at_index = email.find('@')
        dot_index = email.find('.', at_index + 1)
        return at_index != -1 and dot_index != -1 and dot_index != len(email) - 1

    return list(filter(is_valid, emails))