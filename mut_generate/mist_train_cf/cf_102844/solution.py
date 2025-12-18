"""
QUESTION:
Create a function `extract_names` that takes a string `full_name` as input and returns the first and last names. The first name should start with an uppercase letter and the last name should start with a lowercase letter. The input string is assumed to contain at least two words separated by a space, representing the full name.
"""

def extract_names(full_name):
    # Split the full name into a list of words
    words = full_name.split()

    # Extract the first and last names from the list
    first_name = words[0]
    last_name = words[-1]

    # Ensure the first name starts with an uppercase letter
    first_name = first_name.capitalize()

    # Ensure the last name starts with a lowercase letter
    last_name = last_name.lower()

    return first_name, last_name