"""
QUESTION:
Create a function called `validate_message` that takes one string parameter `message`. The function should check the input message and return an error if it exceeds 100 characters in length, contains non-alphabetic characters, or does not contain at least one uppercase letter and one lowercase letter. If the message is valid, the function should return the message with all non-alphabetic characters removed.
"""

import re

def validate_message(message):
    if len(message) > 100:
        return "Error: Message length exceeds 100 characters."
    message = re.sub('[^A-Za-z]', '', message)
    if not any(char.isupper() for char in message) or not any(char.islower() for char in message):
        return "Error: Message must contain at least one uppercase and one lowercase letter."
    return message