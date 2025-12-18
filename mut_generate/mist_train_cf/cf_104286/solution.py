"""
QUESTION:
Write a function called `get_oldest_employees` that takes a list of JSON objects representing employees, where each employee has 'first_name', 'last_name', and 'age' fields. The function should return a dictionary with two keys: 'oldest_employee' and 'top_three_oldest', where 'oldest_employee' is the full name of the employee with the highest age and 'top_three_oldest' is a list of the full names of the top three oldest employees in descending order of their age.
"""

def get_oldest_employees(employees):
    """
    This function takes a list of dictionaries representing employees and returns a dictionary with two keys: 
    'oldest_employee' and 'top_three_oldest', where 'oldest_employee' is the full name of the employee with the highest age 
    and 'top_three_oldest' is a list of the full names of the top three oldest employees in descending order of their age.

    Args:
        employees (list): A list of dictionaries representing employees.

    Returns:
        dict: A dictionary with 'oldest_employee' and 'top_three_oldest' keys.
    """
    
    # Sort employees based on age in descending order
    sorted_employees = sorted(employees, key=lambda x: x['age'], reverse=True)

    # Get the full name of the employee with the highest age
    full_name_highest_age = sorted_employees[0]['first_name'] + ' ' + sorted_employees[0]['last_name']

    # Get the full names of the top three oldest employees
    full_names_top_three_oldest = [employee['first_name'] + ' ' + employee['last_name'] for employee in sorted_employees[:3]]

    return {'oldest_employee': full_name_highest_age, 'top_three_oldest': full_names_top_three_oldest}