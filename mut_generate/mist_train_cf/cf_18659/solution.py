"""
QUESTION:
Write a function `check_email(email)` that checks if the given email address is valid according to the following rules:
- Contains an "@" symbol and a "."
- Has at least 6 characters
- Starts with a letter
- Only contains letters, digits, ".", "@", and "_"
- Does not contain consecutive ".", "@", or "_"
- Does not start or end with ".", "@", or "_"
- Does not have a "." immediately after the "@"
- Has at least one letter before the "@"
- Has at least two letters after the last "."
- Does not have consecutive letters in the domain part
- Does not have more than one "@", ".", or "_"
"""

def check_email(email):
    """
    Checks if the given email address is valid according to the following rules:
    - Contains an "@" symbol and a "."
    - Has at least 6 characters
    - Starts with a letter
    - Only contains letters, digits, ".", "@", and "_"
    - Does not contain consecutive ".", "@", or "_"
    - Does not start or end with ".", "@", or "_"
    - Does not have a "." immediately after the "@"
    - Has at least one letter before the "@"
    - Has at least two letters after the last "."
    - Does not have consecutive letters in the domain part
    - Does not have more than one "@", ".", or "_"

    Args:
        email (str): The email address to be checked.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """

    if "@" not in email:
        return False
    if "." not in email:
        return False
    if len(email) < 6:
        return False
    if not email[0].isalpha():
        return False
    special_chars = [".", "@", "_"]
    for char in email:
        if not char.isalnum() and char not in special_chars:
            return False
    if ".." in email or "@@" in email or "__" in email:
        return False
    if email.count(".") > 1 or email.count("@") > 1 or email.count("_") > 1:
        return False
    if email[email.index("@") + 1] == ".":
        return False
    if not any(char.isalpha() for char in email.split("@")[0]):
        return False
    if len(email.split(".")[-1]) < 2:
        return False
    if email[0] in special_chars or email[-1] in special_chars:
        return False
    domain = email.split("@")[1]
    for i in range(len(domain)-1):
        if domain[i] == domain[i+1]:
            return False
    return True