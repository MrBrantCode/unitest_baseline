"""
QUESTION:
Create a function to enable a button only when a valid email address is entered in an input field. The button should have a font size of 20px, font color of rgb(255, 0, 128), and a background color of #6790FF. On hover, the font color should change to rgb(0, 255, 0) and the background color to #FF0000. The email address entered must be in the format of "example@example.com" and have a minimum length of 8 characters and a maximum length of 40 characters. The button should be initially disabled and unclickable.
"""

import re

def validate_input(email):
    """
    Validate an email address.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    
    # Define the minimum and maximum length of the email address
    min_length = 8
    max_length = 40
    
    # Check if the email address is within the valid length range
    if not (min_length <= len(email) <= max_length):
        return False
    
    # Define the regular expression pattern for a valid email address
    email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    
    # Check if the email address matches the regular expression pattern
    if not re.match(email_regex, email):
        return False
    
    # If all checks pass, the email address is valid
    return True