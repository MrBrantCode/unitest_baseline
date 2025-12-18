"""
QUESTION:
Write a function called `getOldestEmployeeFirstName` that takes a JSON string containing a list of employee objects with 'firstName', 'lastName', and 'age' properties and returns the 'firstName' of the employee with the highest 'age'.
"""

import json

def getOldestEmployeeFirstName(json_data):
    employees = json.loads(json_data)
    sorted_employees = sorted(employees, key=lambda x: x['age'], reverse=True)
    return sorted_employees[0]['firstName']