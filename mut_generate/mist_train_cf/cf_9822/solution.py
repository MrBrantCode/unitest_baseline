"""
QUESTION:
Create a function called create_data_frame that takes a dictionary as input. The dictionary should have the structure of {'state': [...], 'year': [...], 'population': {...}}, where the 'population' key contains a nested dictionary with state names as keys and lists of population data as values. The function should return a data frame where each row represents the population data for a specific state and year combination. The data frame should have three columns: 'state', 'year', and 'population'. The 'state' column should contain the state names, the 'year' column should contain the year values, and the 'population' column should contain the population data for each state and year combination.
"""

import pandas as pd

def create_data_frame(data_dict):
    df = pd.DataFrame({
        'state': data_dict['state'],
        'year': data_dict['year']
    })
    population = pd.DataFrame({
        'state': [key for key, value in data_dict['population'].items() for _ in value],
        'year': [year for key, value in data_dict['population'].items() for year in data_dict['year'][:len(value)]],
        'population': [value for key, value in data_dict['population'].items() for value in value]
    })
    df = pd.merge(df, population, on=['state', 'year'], how='inner')
    return df