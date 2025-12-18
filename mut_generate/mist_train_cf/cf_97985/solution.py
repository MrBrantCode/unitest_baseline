"""
QUESTION:
Write a function `extract_employee_names` that takes a JSON object as input and returns a list of full names of employees. The function should handle nested JSON objects, varying key names, and inconsistent naming conventions within the dataset. The function should also perform data cleaning and normalization by removing duplicates and resolving inconsistencies between data fields.
"""

import json

def extract_employee_names(data, keys_to_check=['name', 'full_name', 'employee_name', 'employee_full_name',
                     'first_name', 'last_name', 'given_name', 'family_name']):
    employee_names = []
    
    if isinstance(data, list):
        # if data is a list, iterate over its items and recursively call extract_employee_names()
        for item in data:
            employee_names.extend(extract_employee_names(item, keys_to_check))
    elif isinstance(data, dict):
        # if data is a dictionary, iterate over its keys and recursively call extract_employee_names()
        for key, value in data.items():
            if key in keys_to_check:
                # if key is one of the identified key names, add the value to employee_names
                employee_names.append(value)
            elif isinstance(value, dict) or isinstance(value, list):
                # if value is a dictionary or a list, recursively call extract_employee_names()
                employee_names.extend(extract_employee_names(value, keys_to_check))
    
    return employee_names