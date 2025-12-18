"""
QUESTION:
Create a function named `create_student_dataframe` that takes a dictionary of students as input, where each student has a 'Name', 'Age', 'Grade Level', and 'Favorite Subject'. The 'Age' must be between 16 and 20 (inclusive), the 'Grade Level' must be between 9 and 13 (inclusive), and the 'Favorite Subject' must be a string of at least 5 characters and at most 30 characters. The function should return a pandas DataFrame sorted by the student's 'Age' in ascending order.
"""

import pandas as pd

def create_student_dataframe(students):
    """
    Create a pandas DataFrame from a dictionary of students, filtering and sorting the data.

    Parameters:
    students (dict): A dictionary where each student has a 'Name', 'Age', 'Grade Level', and 'Favorite Subject'.

    Returns:
    pandas.DataFrame: A DataFrame sorted by the student's 'Age' in ascending order.
    """
    df = pd.DataFrame(students)
    df = df[(df['Age'] >= 16) & (df['Age'] <= 20) & 
            (df['Grade Level'] >= 9) & (df['Grade Level'] <= 13) & 
            (df['Favorite Subject'].str.len() >= 5) & (df['Favorite Subject'].str.len() <= 30)]
    return df.sort_values(by='Age', ascending=True)