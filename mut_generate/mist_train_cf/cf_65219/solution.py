"""
QUESTION:
Write a function `make_employee` that creates a new employee data structure with `name` and `age` attributes and another function `introduce` that takes an employee data structure and returns a string introducing the employee. Ensure the employee data structure and the `introduce` function behave similarly to an object-oriented Employee class, but in a functional programming paradigm. The `make_employee` function should return a dictionary representing the employee, and the `introduce` function should access the employee's name and age from this dictionary to construct the introduction string.
"""

def make_employee(name, age):
    return {'name': name, 'age': age}

def introduce(employee):
    return f"My name is {employee['name']} and I am {employee['age']} years old."