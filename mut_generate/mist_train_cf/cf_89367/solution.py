"""
QUESTION:
Create a function named `my_function` that takes two parameters, `name` and `email`, and returns `None`. The `name` parameter should be a string that cannot be empty. The `email` parameter should be a string, must contain at least 5 characters, and must be a valid email address. The function should validate the `email` parameter using regular expressions.
"""

import re

def entrance(name: str, email: str) -> None:
    if len(name) == 0:
        print("Name cannot be empty.")
        return
    if len(email) < 5:
        print("Email must contain at least 5 characters.")
        return
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        print("Invalid email address.")
        return
    # Rest of the function logic goes here