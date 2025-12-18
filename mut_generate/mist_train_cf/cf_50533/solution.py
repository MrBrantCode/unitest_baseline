"""
QUESTION:
Write a function to create an employee record and another function to retrieve the employee's information. The employee record should contain the name, age, and department of the employee. The get_info function should return a string in the format 'Name: {name}, Age: {age}, Department: {department}'.
"""

def create_employee(name, age, department):
    return {'name': name, 'age': age, 'department': department}

def get_employee_info(employee):
    return f'Name: {employee["name"]}, Age: {employee["age"]}, Department: {employee["department"]}'