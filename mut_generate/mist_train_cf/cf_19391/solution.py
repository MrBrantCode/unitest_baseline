"""
QUESTION:
Write a function `process_message(message)` that takes a string `message` as input, filters out non-alphabetic characters, and returns the filtered string. The function should also enforce a maximum length of 100 characters for the input message, returning an error message if the length exceeds this limit.
"""

import re

def process_message(message):
    if len(message) > 100:
        return "Error: Message exceeds the maximum limit of 100 characters."
    
    message = re.sub(r'[^a-zA-Z]', '', message)
    
    return message