"""
QUESTION:
Write a function named `sum_name_length` that calculates the total length of names in a list, excluding names that start with a lowercase letter and names containing non-alphabetic characters.
"""

def sum_name_length(names):
    total_length = 0
    for name in names:
        if name[0].isupper() and name.isalpha():
            total_length += len(name)
    return total_length