"""
QUESTION:
Write a function `string_checks` that takes a string as input, checks if its length is at least 15 characters and contains at least 3 numerical digits, and returns the 9th and 10th characters of the string if both conditions are met; otherwise, return an error message.
"""

def string_checks(user_string):
    # Check minimum length
    if len(user_string) < 15:
        return "Error: string needs to be at least 15 characters long"

    # Check for at least 3 digits
    num_digits = sum(c.isdigit() for c in user_string)
    if num_digits < 3:
        return "Error: string needs to contain at least 3 digits"

    # Return the 9th and 10th characters (Python counts from 0)
    return user_string[8:10]