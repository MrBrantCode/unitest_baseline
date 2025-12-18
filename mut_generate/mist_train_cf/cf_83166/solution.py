"""
QUESTION:
Write a function `make_employee`, `give_raise`, and `display_employee` to simulate an employee class using functional programming principles. `make_employee` should take `name` and `salary` as input and return an employee dictionary. `give_raise` should take an `employee` dictionary and a `raise_amount` as input, and return a new employee dictionary with the updated salary. `display_employee` should take an `employee` dictionary as input and return a formatted string with the employee's name and salary. The employee data should be treated as immutable, with changes made by creating new dictionaries rather than modifying existing ones.
"""

def make_employee(name, salary):
    return {'name': name, 'salary': salary}

def give_raise(employee, raise_amount):
    return {'name': employee['name'], 'salary': employee['salary'] + raise_amount}

def display_employee(employee):
    return f'{employee["name"]}: {employee["salary"]}'