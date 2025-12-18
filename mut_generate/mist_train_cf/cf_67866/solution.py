"""
QUESTION:
Create a Python function `validate_email(email)` that takes an email address as input and returns a boolean value indicating whether the email is valid or not. The email validation should follow these rules:

* The local-part may only contain alphanumeric characters, underscores, hyphens, and periods.
* No consecutive periods are allowed in the local-part.
* The domain part must be a top-level domain with a maximum length of 6.
* The email must contain the "@" symbol between the local-part and the domain.
* The email must not start with a special character.
* The function should return True if the email is valid, and False otherwise.
"""

import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9][a-zA-Z0-9._-]*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}$'
    if re.match(regex,email) and '..' not in email:
        return True
    return False