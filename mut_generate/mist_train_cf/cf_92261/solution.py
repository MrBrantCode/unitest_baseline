"""
QUESTION:
Implement three functions: `create_employee(name, age)`, `print_details(employee)`, and `sort_employees(employees, compare_func)`. 

`create_employee(name, age)` should create a dictionary representing an employee with the given name and age. 

`print_details(employee)` should return a string in the format "Name: {name}, age: {age}" containing the employee's details.

`sort_employees(employees, compare_func)` should take a list of employee dictionaries and a comparison function as parameters, and return a new list of employees sorted in ascending order based on their age. The sorting algorithm should be stable and have a time complexity of O(n log n). The comparison function should define the ordering of the employees based on their age.
"""

def create_employee(name, age):
    return {"name": name, "age": age}

def print_details(employee):
    return f"Name: {employee['name']}, age: {employee['age']}"

def entrance(employees, compare_func):
    return sorted(employees, key=compare_func)