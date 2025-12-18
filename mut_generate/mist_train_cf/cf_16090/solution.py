"""
QUESTION:
Write a function `calculate_total_salary` that calculates the total salary of employees whose salary is between 40,000 and 50,000, age is between 30 and 40, and department is "Sales". The function takes a list of employee dictionaries as input, where each dictionary contains the employee's name, age, salary, and department.
"""

def calculate_total_salary(employees):
    total_salary = 0
    for employee in employees:
        if 40000 <= employee["salary"] <= 50000 and 30 <= employee["age"] <= 40 and employee["department"] == "Sales":
            total_salary += employee["salary"]
    return total_salary