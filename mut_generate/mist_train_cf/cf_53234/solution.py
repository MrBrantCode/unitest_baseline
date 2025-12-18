"""
QUESTION:
Design a function `name_format` that takes three string parameters: `first_name`, `middle_name`, and `last_name`. The function should remove leading and trailing spaces from the inputs, then return a formatted string in the format `middle_name + space + first letter of first_name + period + space + last_name`. The function should be case-sensitive and handle null or single-letter parameter values effectively.
"""

def name_format(first_name, middle_name, last_name):
    # remove leading and trailing spaces
    first_name = first_name.strip()
    middle_name = middle_name.strip()
    last_name = last_name.strip()

    # check if name values are not null
    if first_name and middle_name and last_name:
        return middle_name + ' ' + first_name[0] + '. ' + last_name
    else:
        return "Invalid input. All fields are required."