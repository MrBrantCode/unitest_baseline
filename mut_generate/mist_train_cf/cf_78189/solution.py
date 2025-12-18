"""
QUESTION:
Create a function named `get_total_salary_range` that takes a list of employees, a minimum salary, a maximum salary, and a department ID as parameters. Each employee is represented as an object with `name`, `salary`, and `department_id` attributes. The function should return the total salary of all employees in the specified department whose salary falls within the given range. The range is inclusive.
"""

def get_total_salary_range(employees, min_salary, max_salary, department_id):
    """
    Calculate the total salary of employees in a specified department 
    whose salary falls within a given range.

    Args:
        employees (list): A list of dictionaries, where each dictionary represents an employee.
        min_salary (int): The minimum salary (inclusive) of the range.
        max_salary (int): The maximum salary (inclusive) of the range.
        department_id (int): The ID of the department.

    Returns:
        int: The total salary of employees in the specified department whose salary is within the given range.
    """
    total_salary = 0
    for employee in employees:
        if (employee['department_id'] == department_id and 
            min_salary <= employee['salary'] <= max_salary):
            total_salary += employee['salary']
    return total_salary