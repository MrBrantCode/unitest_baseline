"""
QUESTION:
Write a function that takes a single string input from the user, checks if it is alphanumeric and has a maximum length of 50 characters, and returns its length if valid or 'Invalid input' otherwise. The function should be written in a single line of code using a lambda function.
"""

def validate_input(s):
    return len(s) if s.isalnum() and len(s) <= 50 else 'Invalid input'