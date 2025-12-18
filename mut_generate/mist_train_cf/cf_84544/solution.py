"""
QUESTION:
Write a function called `user_input` that takes a single character as input and returns a string. The function should return "Monthly" if the input is "M" or "m", "Yearly" if the input is "Y" or "y", and "Invalid" otherwise.
"""

def user_input(char):
    if char.lower() == "m":
        return "Monthly"
    elif char.lower() == "y":
        return "Yearly"
    else:
        return "Invalid"