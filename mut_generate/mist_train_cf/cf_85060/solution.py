"""
QUESTION:
Construct a function named `format_name` that takes three parameters: `first_name`, `middle_name`, and `last_name`. The function should return a string in the format: middle name, followed by a space, the first letter of the first name, a period, another space, and then the last name.
"""

def format_name(first_name, middle_name, last_name):
    return middle_name + ' ' + first_name[0] + '. ' + last_name