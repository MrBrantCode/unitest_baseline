"""
QUESTION:
Write a Python function `median_salary_diff` that takes a list of dictionaries as input, where each dictionary contains an employee's name and salary. The function should compute the median of the absolute salary differences between each employee and the average salary of all employees.
"""

import statistics

def median_salary_diff(employees):
    salaries = [employee['salary'] for employee in employees]
    avg_salary = statistics.mean(salaries)
    diffs = [abs(employee['salary'] - avg_salary) for employee in employees]
    median_diff = statistics.median(diffs)
    return median_diff