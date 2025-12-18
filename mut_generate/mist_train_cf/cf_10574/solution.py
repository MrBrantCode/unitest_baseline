"""
QUESTION:
Write a function `find_oldest_employee_first_name` that takes a JSON string of employee data as input. Each employee object in the JSON string contains 'firstName', 'lastName', and 'age' fields. The function should parse the JSON data, find the employee with the highest age, and return their first name. The input JSON string is a list of employee objects.
"""

import json

def find_oldest_employee_first_name(json_data):
    """
    This function takes a JSON string of employee data as input, parses the data, 
    finds the employee with the highest age, and returns their first name.
    
    Args:
        json_data (str): A JSON string containing a list of employee objects.
        
    Returns:
        str: The first name of the employee with the highest age.
    """
    employees = json.loads(json_data)
    sorted_employees = sorted(employees, key=lambda x: x['age'], reverse=True)
    return sorted_employees[0]['firstName']