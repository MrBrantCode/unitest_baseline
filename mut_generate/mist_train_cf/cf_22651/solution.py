"""
QUESTION:
Create a function `validate_name` that takes a string `name` as input and returns a boolean value indicating whether the name is valid or not. The function should ensure that the name is not empty or just spaces, contains only alphabetical characters, and does not exceed 20 characters in length. If the name is invalid, the function should print an error message describing the reason for the invalidation.
"""

def validate_name(name):
    if len(name) == 0 or name.isspace():
        print("Error: Name cannot be empty or just spaces")
        return False
    if not name.isalpha():
        print("Error: Name should only contain alphabetical characters")
        return False
    if len(name) > 20:
        print("Error: Name cannot exceed 20 characters")
        return False
    return True