"""
QUESTION:
Create a function named `validate_message` that takes a string as input and returns a boolean value indicating whether the string matches a specific pattern. The pattern requires the string to start with "Hey", followed by a space, then a word that begins with a capital letter, and ends with a punctuation mark (period, exclamation point, or question mark).
"""

import re

def validate_message(message):
    # Create a regular expression that matches the described criteria
    regex = r"^Hey [A-Z][a-zA-Z]*[.!?]$"
    # Validate if the given string matches the regular expression
    match = re.match(regex, message)

    if match:
        return True
    else:
        return False