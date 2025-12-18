"""
QUESTION:
Create a function `classify_email` that takes in an email subject as input and returns 'spam' or 'not spam' based on the given rules. The classification rules are as follows:

- If the subject contains 'Get' or 'discount', classify as 'spam'.
- If the subject contains 'Hello' or 'friend', classify as 'not spam'.
- Otherwise, classify as 'spam'.
"""

def classify_email(email_subject):
    """
    Classify an email as 'spam' or 'not spam' based on its subject.

    Args:
        email_subject (str): The subject of the email.

    Returns:
        str: 'spam' or 'not spam'
    """
    if 'Get' in email_subject or 'discount' in email_subject:
        return 'spam'
    elif 'Hello' in email_subject or 'friend' in email_subject:
        return 'not spam'
    else:
        return 'spam'