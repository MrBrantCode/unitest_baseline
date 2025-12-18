"""
QUESTION:
Create a function named `sanitize_input` that takes a string `user_input` as input and returns a sanitized string. The sanitized string should only contain alphanumeric characters and spaces, be no longer than 100 characters, have no leading or trailing spaces, and be in lowercase. If the input exceeds 100 characters, truncate it to 100 characters and remove any incomplete words.
"""

def sanitize_input(user_input):
    # Remove leading and trailing spaces
    user_input = user_input.strip()

    # Check if input is empty
    if len(user_input) == 0:
        return ""

    # Truncate input if it exceeds 100 characters
    if len(user_input) > 100:
        user_input = user_input[:100]

    # Remove special characters and punctuation marks
    sanitized_text = ""
    for char in user_input:
        if char.isalnum() or char.isspace():
            sanitized_text += char

    # Convert sanitized text to lowercase
    sanitized_text = sanitized_text.lower()

    return sanitized_text