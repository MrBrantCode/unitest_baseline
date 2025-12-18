"""
QUESTION:
Create a function called `employee_operations` that takes a pandas DataFrame as input. The DataFrame contains information about employees with the following columns: 'First Name', 'Last Name', 'Age', 'Job Title', 'Salary', 'Years of Experience', and 'Department'. The function should perform the following operations:
- Sort the employees based on their last name in ascending order.
- Calculate the average age of the employees.
- Filter the employees based on 'Job Title' being 'Engineer' and 'Department' being 'Engineering' and create a new DataFrame.
- Calculate the total salary for all employees in each department.
- Find the employee with the highest salary in each department.
- Calculate the average years of experience for employees in each job title category and department.

The function should return the results of all these operations.
"""

import pandas as pd

def employee_operations(df):
    """
    Perform various operations on the input DataFrame containing employee information.
    
    Parameters:
    df (pd.DataFrame): DataFrame with columns 'First Name', 'Last Name', 'Age', 'Job Title', 'Salary', 'Years of Experience', and 'Department'.
    
    Returns:
    tuple: A tuple containing the results of the operations.
    """
    # Sort employees based on last name in ascending order
    sorted_df = df.sort_values(by='Last Name')
    
    # Calculate the average age of the employees
    avg_age = df['Age'].mean()
    
    # Filter employees based on job title and department and create a new dataframe
    filtered_df = df[(df['Job Title'] == 'Engineer') & (df['Department'] == 'Engineering')]
    
    # Calculate the total salary for all employees in each department
    total_salary = df.groupby('Department')['Salary'].sum()
    
    # Find the employee with the highest salary in each department
    highest_salary_employee = df.groupby('Department')['Salary'].idxmax()
    highest_salary_df = df.loc[highest_salary_employee]
    
    # Calculate the average years of experience for employees in each job title category and department
    avg_experience = df.groupby(['Job Title', 'Department'])['Years of Experience'].mean()
    
    return sorted_df, avg_age, filtered_df, total_salary, highest_salary_df, avg_experience