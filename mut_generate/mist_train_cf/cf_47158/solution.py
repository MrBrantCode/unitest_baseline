"""
QUESTION:
Write a function called `validate_user_input` that takes in a string `user_input` and returns the validated input. The function should prevent Cross-Site Scripting (XSS) attacks by ensuring that any special characters in the input are properly escaped. The function should not allow any HTML tags in the input.
"""

import html

def validate_user_input(user_input):
    """
    Validate user input by escaping any special characters to prevent Cross-Site Scripting (XSS) attacks.
    
    Args:
        user_input (str): The input provided by the user.
    
    Returns:
        str: The validated input with special characters escaped.
    """
    return html.escape(user_input)