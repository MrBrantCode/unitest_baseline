"""
QUESTION:
Create a function named `contains_non_alphanumeric` that takes a string `text` as input and returns a boolean value. The function should return `True` if the input text contains at least one non-alphanumeric character, and `False` otherwise.
"""

def contains_non_alphanumeric(text):
    for char in text:
        if not char.isalnum():
            return True
    return False