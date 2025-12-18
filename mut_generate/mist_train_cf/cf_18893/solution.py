"""
QUESTION:
Implement the function `sanitize_input(user_input)` to remove any characters that could be used for SQL injection attacks from the input string, truncate the sanitized string to a maximum length of 50 characters if necessary, and encode the result using base64 encoding.
"""

import base64

def sanitize_input(user_input):
    # Remove potentially harmful characters
    sanitized_input = user_input.replace("'", "").replace('"', '').replace(';', '').replace('\\', '')

    # Truncate to maximum length
    sanitized_input = sanitized_input[:50]

    # Encode using base64
    encoded_input = base64.b64encode(sanitized_input.encode()).decode()

    return encoded_input