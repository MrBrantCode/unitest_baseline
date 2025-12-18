"""
QUESTION:
Modify a given string to ensure it contains at least one special character and one uppercase letter. The function to accomplish this is called `change_data_type`. The input string can be "Hello World!" or any other similar string.
"""

def change_data_type(s):
    """
    Modifies a given string to ensure it contains at least one special character and one uppercase letter.

    Args:
    s (str): The input string.

    Returns:
    str: The modified string with at least one special character and one uppercase letter.
    """
    if not any(not c.isalnum() for c in s):
        s += '!'
    if not any(c.isupper() for c in s):
        s = s.capitalize()
    return s