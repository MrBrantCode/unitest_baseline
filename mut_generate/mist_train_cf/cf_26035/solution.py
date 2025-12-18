"""
QUESTION:
Write a function called `login_attempt` that takes two parameters: `username` and `password`. The function should return `True` if the password is correct and `False` otherwise. The function should also prevent the user from re-submitting the login form until the correct password is entered.
"""

def login_attempt(username, password):
    # Define the correct password
    correct_password = "password123"

    # Check if the password is correct
    if password == correct_password:
        return True
    else:
        return False