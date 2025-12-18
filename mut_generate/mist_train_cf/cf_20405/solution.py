"""
QUESTION:
Write a function `average_top_ten_percent_female_salary` that takes as input a list of dictionaries where each dictionary represents an employee and has the keys 'sex', 'years_worked', and 'salary'. The function should calculate the average salary of the female employees who have worked for at least 5 years and are in the top 10% highest paid employees. Assume that the input list is not empty and contains at least one female employee who has worked for at least 5 years.
"""

import numpy as np

def average_top_ten_percent_female_salary(employees):
    """
    Calculate the average salary of female employees who have worked for at least 5 years and are in the top 10% highest paid employees.

    Args:
        employees (list): A list of dictionaries where each dictionary represents an employee and has the keys 'sex', 'years_worked', and 'salary'.

    Returns:
        float: The average salary of the female employees who have worked for at least 5 years and are in the top 10% highest paid employees.
    """

    # Filter female employees who have worked for at least 5 years
    female_employees = [employee for employee in employees if employee['sex'] == 'female' and employee['years_worked'] >= 5]

    # Extract their salaries
    salaries = [employee['salary'] for employee in female_employees]

    # Calculate the 90th percentile of the salaries to determine the threshold for the top 10%
    threshold = np.percentile(salaries, 90)

    # Filter the salaries that are equal to or above the threshold
    top_salaries = [salary for salary in salaries if salary >= threshold]

    # Calculate the average of the top salaries
    average_salary = sum(top_salaries) / len(top_salaries)

    return average_salary