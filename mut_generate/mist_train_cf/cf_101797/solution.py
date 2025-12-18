"""
QUESTION:
Write a function `calculate_std_dev` that calculates the standard deviation of the length of service for each employee given their start and end dates. The function should take a pandas DataFrame `employment_history` with columns "employee_id", "start_date", and "end_date" as input, where "start_date" and "end_date" are datetime objects. The function should return a dictionary with keys as employee IDs and values as their standard deviation of the length of service in years.
"""

import numpy as np

def calculate_std_dev(employment_history):
    # group employment history by employee ID
    grouped_history = employment_history.groupby('employee_id')
    
    # calculate length of service for each employee
    service_length = grouped_history.apply(lambda x: (x['end_date'] - x['start_date']).dt.days / 365)
    
    # calculate standard deviation of service length for each employee
    std_dev = service_length.apply(lambda x: np.std(x))
    
    # return dictionary with employee IDs as keys and standard deviation of service length as values
    return std_dev.to_dict()