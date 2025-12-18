"""
QUESTION:
Create a function `sanitize_input(user_input)` that takes a string as input, removes any quotes, semicolons, and backslashes, truncates the result to a maximum length of 50 characters, and encodes the result using base64 encoding. The function should return the sanitized and encoded string.
"""

import base64

def sanitize_input(user_input):
    # Remove characters that could be used for SQL injection
    sanitized_input = user_input.replace("'", "").replace(";", "").replace("\\", "")

    # Truncate the input to a maximum length of 50 characters
    sanitized_input = sanitized_input[:50]

    # Encode the sanitized input using base64 encoding
    encoded_input = base64.b64encode(sanitized_input.encode()).decode()

    return encoded_input