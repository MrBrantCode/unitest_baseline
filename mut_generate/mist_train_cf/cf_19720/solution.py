"""
QUESTION:
Write a function `select_employees` to select employee records from a given database table 'employees' with the following conditions: 
- The salary is between 10000 and 50000.
- The department ID is either 1 or 2.
- The last name does not start with the letter 'S'.
"""

def select_employees(employees):
    """
    Select employee records from the 'employees' table based on given conditions.

    Args:
        employees (list of dictionaries): A list of dictionaries, where each dictionary represents an employee record.

    Returns:
        list of dictionaries: A list of selected employee records.
    """
    return [employee for employee in employees 
            if 10000 <= employee['salary'] <= 50000 
            and employee['department_id'] in [1, 2] 
            and not employee['last_name'].startswith('S')]