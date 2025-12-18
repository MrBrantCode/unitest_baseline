"""
QUESTION:
Implement a function `sort_employee_names` that takes a list of employee names as input and returns a new list containing the names that do not start with 'A', sorted in descending order. The input list may contain duplicate names and names with different capitalization. The function should ignore any names that start with 'A' or 'a'.
"""

def sort_employee_names(employee_names):
    """
    Returns a list of employee names that do not start with 'A' or 'a', sorted in descending order.

    Args:
    employee_names (list): A list of employee names.

    Returns:
    list: A list of employee names that do not start with 'A' or 'a', sorted in descending order.
    """
    return sorted([name for name in employee_names if not name.lower().startswith('a')], reverse=True)