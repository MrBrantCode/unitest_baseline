"""
QUESTION:
Write a function `filter_and_sum` that takes a DataFrame `df` and a column name `column` as input. The function should filter out rows with a missing value in the specified column, then return the sum of the 'Salary' column for the remaining rows where 'Age' is greater than 20, 'Name' is alphabetically ordered in descending order, 'Gender' is either 'Male' or 'Female', and 'Nationality' is either 'USA' or 'Canada'.
"""

def filter_and_sum(df, column):
    df = df.dropna(subset=[column])
    df = df[df['Age'] > 20]
    df = df[df['Name'].str.isalpha()]
    df = df[df['Gender'].isin(['Male', 'Female'])]
    df = df[df['Nationality'].isin(['USA', 'Canada'])]
    sum_salary = df['Salary'].sum()
    return sum_salary