"""
QUESTION:
Write a function `find_highest_average_salary` that takes a dictionary where the keys are company names and the values are lists of salaries. Return the name of the company with the highest average salary. Assume the input dictionary is non-empty and all lists of salaries are non-empty.
"""

import statistics

def find_highest_average_salary(salary_data):
    """
    This function calculates the average salary of each company and returns the company with the highest average salary.

    Args:
        salary_data (dict): A dictionary where the keys are company names and the values are lists of salaries.

    Returns:
        str: The name of the company with the highest average salary.
    """
    # calculate the average salary of each company and store it in a dictionary
    average_salaries = {company: statistics.mean(salaries) for company, salaries in salary_data.items()}
    # find the company with the highest average salary
    highest_average_salary_company = max(average_salaries, key=average_salaries.get)
    return highest_average_salary_company