"""
QUESTION:
Create a function `my_function` that takes two parameters: `name` and `email`, both of type string. The `email` parameter must be at least 5 characters long and a valid email address. The function should return an error message if the `email` is invalid or does not meet the length requirement.
"""

import re

def my_function(name: str, email: str) -> None:
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