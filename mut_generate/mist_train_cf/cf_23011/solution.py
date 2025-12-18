"""
QUESTION:
Create a function `validate_name` that takes a string `name` as input and returns `True` if it meets the following conditions:
- The length of the name is exactly 5 characters.
- The first character of the name is a capital letter.
- The name contains at least one lowercase letter.
- The name contains at least one special character (defined as !, @, #, $, %, ^, &, or *).
The function should return `False` otherwise.
"""

def validate_name(name):
    """
    Validate a name based on specific conditions.

    Args:
    name (str): The input name to be validated.

    Returns:
    bool: True if the name is valid, False otherwise.
    """
    return (len(name) == 5) and (name[0].isupper()) and (any(char.islower() for char in name)) and (any(char in '!@#$%^&*' for char in name))