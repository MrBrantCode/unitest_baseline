"""
QUESTION:
Write a function to find all employees that meet the following criteria: age between 25 and 30, department is 'Marketing', and salary is above the average salary of all employees. The function should return a list of tuples, where each tuple contains the employee name and department name. The results should be sorted by employee name in alphabetical order, excluding employees with NULL or empty salaries.
"""

import pandas as pd

def find_marketing_employees(df):
    """
    Finds all employees in the 'Marketing' department who meet the specified criteria.

    Args:
    df (pd.DataFrame): A DataFrame containing employee data.

    Returns:
    list: A list of tuples, where each tuple contains the employee name and department name.
    """
    # Filter out rows with NULL or empty salaries
    df = df[pd.notnull(df['salary']) & (df['salary'] != '')]
    
    # Calculate the average salary
    avg_salary = df['salary'].mean()
    
    # Filter employees based on the given criteria
    marketing_employees = df[(df['age'].between(25, 30)) & 
                            (df['department'] == 'Marketing') & 
                            (df['salary'] > avg_salary)]
    
    # Return a list of tuples containing employee name and department name, sorted by employee name
    return sorted(list(zip(marketing_employees['employee_name'], marketing_employees['department'])))