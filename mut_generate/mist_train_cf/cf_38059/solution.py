"""
QUESTION:
Write a function `average_grades` that takes a pandas DataFrame as input, containing student information with columns 'Name', 'Age', 'Grade', and 'Subject', and returns a dictionary where the keys are the unique subjects and the values are the highest grades obtained for each subject by any student. If a subject has multiple entries for the same student, consider the highest grade obtained for that subject.
"""

import pandas as pd
from typing import Dict

def average_grades(data: pd.DataFrame) -> Dict[str, float]:
    # Group the data by 'Subject' and find the maximum grade for each subject
    max_grades = data.groupby('Subject')['Grade'].max()
    
    # Convert the grouped data to a dictionary
    average_grades_dict = max_grades.to_dict()
    
    return average_grades_dict