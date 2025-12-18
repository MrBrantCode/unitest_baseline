"""
QUESTION:
Create a function named `capitalize_names` that takes a list of strings as input and returns a new list where the first letter of each string is capitalized.
"""

def capitalize_names(names):
    new_names = []
    for name in names:
        new_name = name[0].upper() + name[1:]
        new_names.append(new_name)
    return new_names