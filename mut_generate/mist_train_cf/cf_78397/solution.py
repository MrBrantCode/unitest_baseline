"""
QUESTION:
Write a Python function named `extract_domain_name` that takes an email address as a string and returns the domain name. The domain name is the part of the email address after the '@' symbol.
"""

def extract_domain_name(email):
    """
    Extracts the domain name from an email address.

    Args:
        email (str): The email address.

    Returns:
        str: The domain name.
    """
    return email.split('@')[-1]