"""
QUESTION:
Write a function named `sort_employee_names` that takes a list of employee names as input and returns a new list containing only the names that do not start with the letter 'A', sorted alphabetically. The input list may contain any combination of names.
"""

def sort_employee_names(employee_names):
    """
    Returns a new list containing employee names that do not start with 'A', sorted alphabetically.

    Args:
        employee_names (list): A list of employee names.

    Returns:
        list: A list of employee names that do not start with 'A', sorted alphabetically.
    """
    return sorted([name for name in employee_names if not name.startswith('A')])