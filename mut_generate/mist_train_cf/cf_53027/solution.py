"""
QUESTION:
Create a function `sort_by_age` that takes a list of employee dictionaries as input, where each dictionary contains the keys 'name', 'age', 'salary', and 'department'. The function should return the sorted list of employees in ascending order based on the 'age' field.
"""

def sort_by_age(employees):
    sorted_employees = sorted(employees, key=lambda x: x['age'])
    return sorted_employees