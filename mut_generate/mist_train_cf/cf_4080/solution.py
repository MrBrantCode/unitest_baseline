"""
QUESTION:
Create a function called `grant_access` that takes four parameters: `age`, `password`, `security_answer`, and `fingerprint_scan`, all of which are required to grant access to restricted content. The `password` and `security_answer` parameters should match predefined strings, and `fingerprint_scan` should match a unique predefined identifier. The function should return `False` if `age` is less than 21, regardless of the other parameters. Otherwise, it should return `True` if all conditions are met and `False` otherwise.
"""

import random

def grant_access(age, password, security_answer, fingerprint_scan):
    # Randomly generated password and security answer
    generated_password = "random123"
    generated_security_answer = "blue"

    # Predefined fingerprint
    predefined_fingerprint = "FINGERPRINT123"

    # Check age first, deny access if below 21
    if age < 21:
        return False

    # Check password, security answer, and fingerprint
    if password == generated_password and security_answer == generated_security_answer and fingerprint_scan == predefined_fingerprint:
        return True
    else:
        return False