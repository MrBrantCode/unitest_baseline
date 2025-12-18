"""
QUESTION:
Write a function named `sort_by_salary` that takes a list of employee records as input. Each record is a dictionary containing 'name', 'age', 'salary', and 'department' keys. The function should sort the list in descending order based on the 'salary' of each employee.
"""

def sort_by_salary(employee_records):
    """
    Sorts a list of employee records in descending order based on salary.

    Args:
        employee_records (list): A list of dictionaries containing 'name', 'age', 'salary', and 'department' keys.

    Returns:
        list: The sorted list of employee records.
    """
    return sorted(employee_records, key=lambda x: x['salary'], reverse=True)