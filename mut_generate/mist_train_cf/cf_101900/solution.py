"""
QUESTION:
Write a function `calculate_highest_average_salary` that takes a dictionary `salary_data` where the keys are company names and the values are lists of salaries for each company. Return the company with the highest average salary. The function should handle any number of companies and salaries.
"""

import statistics

def calculate_highest_average_salary(salary_data):
    """
    This function calculates the company with the highest average salary.

    Args:
    salary_data (dict): A dictionary where keys are company names and values are lists of salaries.

    Returns:
    str: The company with the highest average salary.
    """
    
    # Initialize the company with the highest average salary and its average salary
    highest_average_salary_company = None
    highest_average_salary = 0
    
    # Iterate over each company in the salary data
    for company, salaries in salary_data.items():
        # Calculate the average salary of the current company
        average_salary = statistics.mean(salaries)
        
        # Check if the average salary of the current company is higher than the highest average salary found so far
        if average_salary > highest_average_salary:
            # Update the company with the highest average salary and its average salary
            highest_average_salary_company = company
            highest_average_salary = average_salary
    
    # Return the company with the highest average salary
    return highest_average_salary_company