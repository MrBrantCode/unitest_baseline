"""
QUESTION:
Create a function named `validate_message` that takes one argument `message`. The function should return an error if the length of the `message` exceeds 100 characters. It should remove any non-alphabetic characters from the `message`. The function should also check if the `message` contains at least one uppercase and one lowercase letter, and return an error if this condition is not met. If all checks pass, the function should return the cleaned `message`.
"""

import re

def validate_message(message):
    # Check if message length exceeds the limit
    if len(message) > 100:
        return "Error: Message length exceeds 100 characters."

    # Remove non-alphabetic characters from message
    message = re.sub('[^A-Za-z]', '', message)

    # Check if message contains at least one uppercase and one lowercase letter
    if not any(char.isupper() for char in message) or not any(char.islower() for char in message):
        return "Error: Message must contain at least one uppercase and one lowercase letter."

    return message