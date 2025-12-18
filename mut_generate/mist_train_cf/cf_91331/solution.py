"""
QUESTION:
Design a function named `validate_email` that takes a string as input and returns True if it is a valid email address according to the following requirements:

- The email address must start with a combination of alphanumeric characters, followed by an '@' symbol.
- After the '@' symbol, there must be a combination of alphanumeric characters, followed by a dot '.'.
- After the dot '.', there must be a combination of alphabetic characters, with a minimum length of 2 and a maximum length of 6.
- The email address must not exceed a total length of 50 characters.
- The email address must not contain any special characters other than '@' and '.'.
- The email address must not start or end with any special characters.
- The email address must not contain consecutive dots '..' or consecutive '@' symbols.

The function should ignore any leading or trailing whitespaces in the input string.
"""

import re

def validate_email(email):
    # Remove leading and trailing whitespaces
    email = email.strip()

    # Define the regular expression pattern
    pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"

    # Check if the email matches the pattern
    if re.match(pattern, email) and len(email) <= 50:
        # Check for consecutive dots or consecutive @ symbols
        if ".." not in email and "@@" not in email:
            # Check if the email does not start or end with a special character
            if email[0] not in ['@', '.'] and email[-1] not in ['@', '.']:
                return True

    return False