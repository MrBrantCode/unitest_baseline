"""
QUESTION:
Write a function `get_domain_name(email: str) -> str` that takes in a string `email` and verifies if it is a valid email address. If it is valid, the function should return the domain name of the email address. If it is not valid, the function should return an empty string.

A valid email address must have exactly one "@" symbol, at least one character before and after the "@" symbol, at least one "." symbol after the "@" symbol, and only alphanumeric characters and special characters allowed in an email address (e.g., ".", "-", "_") before and after the "@" symbol. The domain name must have at least one character before the first "." symbol and at least one character after the last "." symbol.
"""

def get_domain_name(email: str) -> str:
    """
    This function takes in a string email and verifies if it is a valid email address.
    If it is valid, the function returns the domain name of the email address.
    If it is not valid, the function returns an empty string.

    Args:
        email (str): The input email address.

    Returns:
        str: The domain name of the email address if valid, otherwise an empty string.
    """

    # Check if the email string contains exactly one "@" symbol
    if email.count('@') != 1:
        return ""

    # Split the email string into two parts at the "@" symbol
    local_part, domain_name = email.split('@')

    # Check if both parts have at least one character
    if len(local_part) < 1 or len(domain_name) < 1:
        return ""

    # Split the domain name into two parts at the first "." symbol
    domain_parts = domain_name.split('.')

    # Check if the domain name has at least one "." symbol and both parts have at least one character
    if len(domain_parts) < 2 or len(domain_parts[0]) < 1 or len(domain_parts[-1]) < 1:
        return ""

    # Return the domain name
    return domain_name