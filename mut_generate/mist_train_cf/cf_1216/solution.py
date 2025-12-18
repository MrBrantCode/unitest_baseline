"""
QUESTION:
Generate a function named `generate_class_list` that takes a list of student names as input and returns a list of unique names, sorted in alphabetical order, with the following conditions: 
- Each name is stripped of leading and trailing whitespaces.
- Names containing internal whitespaces are excluded.
- Names are case-insensitive (i.e., 'John' and 'john' are considered the same).
- The returned list does not exceed a length of 10.
"""

def generate_class_list(class_names):
    # Remove leading and trailing whitespaces from each name
    class_names = [name.strip() for name in class_names]

    # Remove any names with whitespace within them
    class_names = [name for name in class_names if ' ' not in name]

    # Convert all names to lowercase to handle case sensitivity
    class_names = [name.lower() for name in class_names]

    # Remove any duplicate names
    class_names = list(set(class_names))

    # Sort the names in alphabetical order
    class_names.sort()

    # Ensure the class list does not exceed a length of 10
    class_names = class_names[:10]

    return class_names