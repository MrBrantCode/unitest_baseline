"""
QUESTION:
Create a function `validate_email` that takes a string as input and returns `True` if it matches a specific email address format and `False` otherwise. The email address should only allow lowercase alphabets, digits, and the special characters: +, -, _, and .. The function should match the start and end of the string and allow one or more occurrences of the character groups. The domain name should allow lowercase alphabets, digits, and the special characters - and .. The top-level domain should have a minimum length of 2.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address format.
    
    Args:
    email (str): The email address to be validated.
    
    Returns:
    bool: True if the email address matches the specified format, False otherwise.
    """
    
    # Define the regex pattern for the email address format
    pattern = r"^[a-z0-9+_.-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    
    # Use the fullmatch function to match the entire string against the pattern
    return bool(re.fullmatch(pattern, email))