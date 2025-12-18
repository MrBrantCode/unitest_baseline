"""
QUESTION:
Write a function named `calculate_std_dev` that takes a table with columns "employee_id", "start_date", and "end_date" as input. The function should calculate the standard deviation of the length of service in years for each employee and return a dictionary with employee IDs as keys and their corresponding standard deviation of service length as values. The function should use NumPy for the standard deviation calculation and the input table is expected to be in a format that allows for grouping by "employee_id" and date subtraction.
"""

import numpy as np
import pandas as pd

def calculate_std_dev(employment_history):
    # group employment history by employee ID
    grouped_history = employment_history.groupby('employee_id')
    
    # calculate length of service for each employee
    service_length = grouped_history.apply(lambda x: (x['end_date'] - x['start_date']).dt.days / 365)
    
    # calculate standard deviation of service length for each employee
    std_dev = service_length.apply(lambda x: np.std(x))
    
    # return dictionary with employee IDs as keys and standard deviation of service length as values
    return std_dev.to_dict()