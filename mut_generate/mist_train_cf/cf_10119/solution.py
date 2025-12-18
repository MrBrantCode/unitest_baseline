"""
QUESTION:
Write a function `validate_name` that takes a string `name` as input and returns a string indicating whether the name is valid or not. The name is valid if it meets the following conditions:
- The name is not empty.
- The name contains only alphabets.
- The length of the name is at most 10 characters.
Return an error message if any of these conditions are not met, and return a success message if all conditions are met.
"""

def validate_name(name):
    if len(name) == 0:
        return "Name cannot be empty."
    if not name.isalpha():
        return "Name should only contain alphabets."
    if len(name) > 10:
        return "Name should be at most 10 characters long."
    return "Name is valid."