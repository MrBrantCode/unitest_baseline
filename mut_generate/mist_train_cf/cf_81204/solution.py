"""
QUESTION:
Create a function `create_employee(name, age)` that returns a dictionary representing an employee with the provided name and age. Then create another function `display_employee(employee)` that takes the employee dictionary and returns a formatted string containing the employee's name and age. Implement exception handling in `display_employee` to handle cases where the employee dictionary is missing required keys. Ensure that the functions work correctly by writing unit tests to verify their behavior. 

Restrictions: The functions should not use object-oriented programming and should be implemented using the functional programming paradigm.
"""

def create_employee(name, age):
    return {'name': name, 'age': age}

def display_employee(employee):
    try:
        result = f"Name: {employee['name']}, Age:{employee['age']}"
    except KeyError:
        result = "Invalid employee data"
    return result