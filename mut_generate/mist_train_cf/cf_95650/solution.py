"""
QUESTION:
Create a function `process_message(message)` that takes a string as input and returns a string. The function should filter out non-alphabetic characters from the message and return an error message if the message exceeds 100 characters after filtering.
"""

import re

def process_message(message):
    if len(message) > 100:
        return "Error: Message exceeds the maximum limit of 100 characters."
    
    message = re.sub(r'[^a-zA-Z]', '', message)
    
    return message