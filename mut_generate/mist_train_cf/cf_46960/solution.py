"""
QUESTION:
Create a function named `sum_name_length` that takes a list of names as input and returns the sum of the lengths of the names that start with an uppercase letter and only contain alphabetic characters. Do not include names that start with a lowercase letter or contain non-alphabetic characters.
"""

def sum_name_length(names):
    total_length = 0
    valid_names = [name for name in names if name[0].isupper() and name.isalpha()]
    for name in valid_names:
        total_length += len(name)
    return total_length