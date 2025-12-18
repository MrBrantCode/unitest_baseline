"""
QUESTION:
Write a function that retrieves the name, age, and salary of the youngest employee with a salary greater than $50,000 from a given dataset. The function should return a single record with the required information.
"""

def youngest_high_salary_employee(employees):
    """
    Retrieves the name, age, and salary of the youngest employee 
    with a salary greater than $50,000 from a given dataset.

    Args:
    employees (list): A list of dictionaries, each containing employee information.

    Returns:
    dict: A dictionary containing the name, age, and salary of the youngest 
          employee with a salary greater than $50,000.
    """
    high_salary_employees = [employee for employee in employees if employee['salary'] > 50000]
    if high_salary_employees:
        return min(high_salary_employees, key=lambda x: x['age'])
    else:
        return None