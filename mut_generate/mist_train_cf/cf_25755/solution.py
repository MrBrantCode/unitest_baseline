"""
QUESTION:
Write a function `find_email` that uses Regular Expressions to extract and return the email address from a given string. The function should take a string as input and return a list of email addresses found in the string. The email addresses should be in the format of a string of alphanumeric characters, dots, and underscores followed by '@' and then another string of alphanumeric characters, dots, and underscores.
"""

import re

def find_email(input_string):
    """
    Extracts and returns the email address from a given string.
    
    Args:
    input_string (str): The string to extract the email address from.
    
    Returns:
    list: A list of email addresses found in the string.
    """
    expression = r'[\w\.-]+@[\w\.-]+'
    return re.findall(expression, input_string)