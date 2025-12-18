"""
QUESTION:
Write a function named `sort_names_by_last_name` that takes a list of names as input and returns a new list with the names sorted by the last name. The function should use a lambda function as the key argument for the built-in `sorted` function. The input list contains names in the format "First Name Last Name".
"""

def sort_names_by_last_name(names):
    return sorted(names, key=lambda name: name.split()[-1])