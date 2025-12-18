"""
QUESTION:
Write a simple regex to validate a username. Allowed characters are:

- lowercase letters,
- numbers,
- underscore

Length should be between 4 and 16 characters (both included).
"""

import re

def validate_username(username: str) -> bool:
    """
    Validates a username based on the following criteria:
    - Allowed characters: lowercase letters, numbers, and underscore.
    - Length should be between 4 and 16 characters (both included).

    Parameters:
    username (str): The username string to be validated.

    Returns:
    bool: True if the username is valid, False otherwise.
    """
    return re.match('^[a-z0-9_]{4,16}$', username) is not None