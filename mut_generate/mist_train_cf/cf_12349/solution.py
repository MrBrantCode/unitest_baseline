"""
QUESTION:
Create three functions: `create_employee`, `print_details`, and `sort_employees`. 

`create_employee` should take two parameters, `name` and `age`, and return a dictionary containing the employee's information.

`print_details` should take an employee dictionary and return a string in the format "Name: {name}, age: {age}".

`sort_employees` should take a list of employee dictionaries and a comparison function as parameters. It should return a new list of employees sorted by their age in ascending order using a stable sorting algorithm with a time complexity of O(n log n), such as merge sort or Timsort. The comparison function should define the ordering of the employees based on their age.
"""

def create_employee(name, age):
    return {"name": name, "age": age}

def print_details(employee):
    return f"Name: {employee['name']}, age: {employee['age']}"

def sort_employees(employees):
    return sorted(employees, key=lambda e: e["age"])