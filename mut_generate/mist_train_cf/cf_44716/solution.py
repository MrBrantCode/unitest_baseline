"""
QUESTION:
Create a function called `sum_name_length` that takes a list of names as input, calculates the cumulative length of names that start with an uppercase letter and contain only alphabetic characters, and returns the total length. The function should not modify the original list.
"""

def sum_name_length(names):
    total_length = 0
    for name in names:
        if not name[0].isupper() or not name.isalpha():
            continue
        total_length += len(name)
    return total_length