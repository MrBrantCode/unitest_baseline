"""
QUESTION:
Implement a function `validate_email_subject(subject: str) -> bool` that takes a string `subject` as input and returns `True` if the subject is deemed appropriate for sending the email, and `False` if the subject is inappropriate. Ensure that the function checks for the following inappropriate content:
- Any offensive language or profanity
- Sensitive or personal information such as credit card numbers, social security numbers, or passwords.
"""

import re

def validate_email_subject(subject: str) -> bool:
    # Check for offensive language or profanity
    offensive_words = ["offensive_word1", "offensive_word2", "offensive_word3"]  # Add more offensive words as needed
    for word in offensive_words:
        if word in subject.lower():
            return False

    # Check for sensitive information using regular expressions
    sensitive_patterns = [
        r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b',  # Credit card number pattern
        r'\b\d{3}[\s-]?\d{2}[\s-]?\d{4}\b',  # Social security number pattern
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Email address pattern
    ]
    for pattern in sensitive_patterns:
        if re.search(pattern, subject):
            return False

    return True