"""
QUESTION:
Write a function `filter_and_sum(df, column)` that takes a pandas DataFrame `df` and a column name `string` as inputs. The function should filter out rows with missing values in the specified `column`, then filter rows where 'Age' is greater than 20 and 'Gender' is either "Male" or "Female". It should also sort the remaining rows by 'Name' in descending order, but this is not a requirement for the output. Finally, it should return the sum of the 'Salary' column for the remaining rows.
"""

import pandas as pd

def entrance(df, column):
    # Filter out rows with missing values in the specified column
    df = df.dropna(subset=[column])
    
    # Filter out rows where Age is less than or equal to 20
    df = df[df['Age'] > 20]
    
    # Filter out rows where Gender is not "Male" or "Female"
    df = df[df['Gender'].isin(['Male', 'Female'])]
    
    # Sort rows by Name in descending order
    df = df.sort_values(by='Name', ascending=False)
    
    # Compute the sum of the Salary column
    salary_sum = df['Salary'].sum()
    
    return salary_sum