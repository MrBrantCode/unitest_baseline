"""
QUESTION:
Write a function `sort_employees` that takes a list of employee records as input, where each record is a dictionary with keys 'name', 'age', 'salary', and 'department'. Sort the list in descending order based on salary and ascending order based on age. Return the sorted list.
"""

def sort_employees(employees):
    return sorted(employees, key=lambda x: (-x['salary'], x['age']))