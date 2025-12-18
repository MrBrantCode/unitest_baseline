"""
QUESTION:
Write a function named `filter_employee_names` that takes a list of employee names as input and returns a new list containing names that do not start with the letter 'A', sorted in descending alphabetical order, and with a maximum length of 5 characters.
"""

def filter_employee_names(employee_names):
    """
    Filters a list of employee names, removing those starting with 'A', 
    sorting the rest in descending order, and keeping only names with 5 characters or less.

    Args:
        employee_names (list): A list of employee names

    Returns:
        list: A filtered list of employee names
    """
    return sorted([name for name in employee_names if not name.startswith('A') and len(name) <= 5], reverse=True)