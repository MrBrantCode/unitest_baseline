"""
QUESTION:
Write a function `get_top_employees` that takes a list of JSON objects representing employees with 'id', 'first_name', 'last_name', and 'age' keys. Return a tuple containing the full name of the employee with the highest age and a list of full names of the top three oldest employees. The function should sort the employees in descending order based on their age.
"""

import json

def get_top_employees(employees):
    """
    This function takes a list of JSON objects representing employees with 'id', 'first_name', 'last_name', and 'age' keys.
    It returns a tuple containing the full name of the employee with the highest age and a list of full names of the top three oldest employees.

    :param employees: A list of JSON objects representing employees
    :return: A tuple containing the full name of the employee with the highest age and a list of full names of the top three oldest employees
    """
    # Parse JSON objects into a list
    employees = json.loads(employees)

    # Sort employees based on age in descending order
    sorted_employees = sorted(employees, key=lambda x: x['age'], reverse=True)

    # Get the full name of the employee with the highest age
    highest_age_employee = sorted_employees[0]
    full_name_highest_age = highest_age_employee['first_name'] + ' ' + highest_age_employee['last_name']

    # Get the full names of the top three oldest employees
    top_three_oldest = sorted_employees[:3]
    full_names_top_three_oldest = [employee['first_name'] + ' ' + employee['last_name'] for employee in top_three_oldest]

    return (full_name_highest_age, full_names_top_three_oldest)