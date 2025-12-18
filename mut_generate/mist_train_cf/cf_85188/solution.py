"""
QUESTION:
Create a function called `is_valid_input` that takes a string as input and returns `True` if the string is a digit and `False` otherwise. Using this function, simulate a do-while loop that continuously prompts the user to enter a positive number until a valid input is provided.
"""

def is_valid_input(user_input):
    # This is a uniquely designed function that checks if the input is valid
    if user_input.isdigit():
        return True
    else:
        return False