"""
QUESTION:
Write a function named `calculate_gross_salary` that calculates the gross salary of an employee. The gross salary is calculated by adding the basic salary of 10,000 and the allowance of 4,000 to the bonus and subtracting the deductions. The bonus and deductions may vary for each employee.
"""

def calculate_gross_salary(bonus, deduction):
    basic_salary = 10000
    allowance = 4000
    gross_salary = basic_salary + allowance + bonus - deduction
    return gross_salary