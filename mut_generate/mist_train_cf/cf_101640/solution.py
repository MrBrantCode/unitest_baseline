"""
QUESTION:
Write a function `calculate_std_dev` that takes a table of employee data as input and returns a dictionary with employee IDs as keys and their standard deviation of the length of service in years as values. The table contains columns "employee_id", "start_date", and "end_date", where "start_date" and "end_date" are dates. The length of service is calculated as the difference between the end and start dates in years. Assume that an employee may have multiple entries in the table.
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