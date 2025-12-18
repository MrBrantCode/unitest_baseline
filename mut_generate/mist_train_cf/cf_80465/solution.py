"""
QUESTION:
Create a functional programming version of an employee management system that maintains employee data as a list of dictionaries and provides functions for hiring, promoting, and incrementing salaries. Each function should return a new representation of the data without mutating the original data. Ensure error handling for cases such as hiring an existing employee, promoting or incrementing the salary of a non-existent employee, and exceeding the maximum salary limit. Implement comprehensive unit tests to validate the functionality. 

The functions should be named as follows:
- `hire_employee(employee_data, name, age, position, salary)`
- `promote(employee_data, name, position)`
- `increment_salary(employee_data, name, salary_increment)`

Assume a maximum salary limit of 1 million.
"""

import copy

def hire_employee(employee_data, name, age, position, salary):
    if name in [emp['name'] for emp in employee_data]:
        return 'Employee already exists!'
    new_employee = {'name': name, 'age': age, 'position': position, 'salary': salary}
    return employee_data + [new_employee]

def promote(employee_data, name, position):
    for i, emp in enumerate(employee_data):
        if emp['name'] == name:
            new_emp = copy.deepcopy(emp)
            new_emp['position'] = position
            return employee_data[:i] + [new_emp] + employee_data[i+1:]
    return 'Employee not found!'

def increment_salary(employee_data, name, salary_increment):
    for i, emp in enumerate(employee_data):
        if emp['name'] == name:
            new_emp = copy.deepcopy(emp)
            new_emp['salary'] += salary_increment
            if new_emp['salary'] > 1000000: 
                return 'Salary limit exceeded!'
            return employee_data[:i] + [new_emp] + employee_data[i+1:]
    return 'Employee not found!'