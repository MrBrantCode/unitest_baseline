"""
QUESTION:
Create a function called `reverse_name_order` that takes a string as input and returns the first and last name in the string in reversed order. The input string may contain other words besides the first and last name. The function should return an error message if the string does not contain at least two names.
"""

def reverse_name_order(greeting):
    # split the string into words
    words = greeting.split()
    # check if the string has at least two names
    if len(words) < 2:
        return "Invalid input. At least two names are required."
    # extract the first name and last name
    first_name = words[-2]
    last_name = words[-1]
    # reverse the order
    result = last_name + " " + first_name
    return result