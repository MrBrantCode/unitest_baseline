"""
QUESTION:
Create a function `dict_to_dataframe(dictionary)` that takes a dictionary and returns a data frame. The dictionary has three keys: 'state', 'year', and optionally 'population'. The 'population' key contains a nested dictionary where the keys are states and the values are lists of population data for each year. 

The function should have a time complexity of O(n), where n is the total number of population data points in the dictionary, and a space complexity of O(m), where m is the number of unique state-year combinations in the dictionary. If the 'population' key is not present, the function should still return a data frame with 'state' and 'year' columns.
"""

import pandas as pd

def dict_to_dataframe(dictionary):
    if 'population' in dictionary:
        data = []
        for state in dictionary['population']:
            for i, year in enumerate(dictionary['year']):
                data.append([state, year, dictionary['population'][state][i]])
        df = pd.DataFrame(data, columns=['state', 'year', 'population'])
    else:
        df = pd.DataFrame({'state': dictionary['state'], 'year': dictionary['year']})
    return df