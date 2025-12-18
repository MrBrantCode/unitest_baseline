"""
QUESTION:
Given a dictionary of company names as keys and lists of salaries as values, write a function named `find_highest_average_salary` that calculates the average salary of each company and returns the company with the highest average salary. The function should take one parameter, `salary_data`, which is the dictionary containing company names and their respective salary data.
"""

import statistics

def find_highest_average_salary(salary_data):
    """
    This function calculates the average salary of each company 
    and returns the company with the highest average salary.

    Args:
        salary_data (dict): A dictionary containing company names as keys 
            and lists of salaries as values.

    Returns:
        str: The company with the highest average salary.
    """
    highest_average = 0
    company_with_highest_average = ""

    for company, salaries in salary_data.items():
        average_salary = statistics.mean(salaries)
        if average_salary > highest_average:
            highest_average = average_salary
            company_with_highest_average = company

    return company_with_highest_average