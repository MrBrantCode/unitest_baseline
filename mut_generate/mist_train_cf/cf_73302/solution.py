"""
QUESTION:
Create a function `flatten_kinesis_stream_data` that takes a list of dictionaries as input. Each dictionary contains 'customer_id', 'sensor_id', 'timestamps', and 'values'. The function should return a pandas DataFrame where the 'timestamps' and 'values' arrays are flattened into rows, and each row corresponds to a unique combination of 'customer_id', 'sensor_id', 'timestamp', and 'value'. The function assumes that 'timestamps' and 'values' have the same length.
"""

import pandas as pd
from itertools import chain

def flatten_kinesis_stream_data(data):
    """
    This function takes a list of dictionaries as input, where each dictionary contains 
    'customer_id', 'sensor_id', 'timestamps', and 'values'. It returns a pandas DataFrame 
    where the 'timestamps' and 'values' arrays are flattened into rows, and each row 
    corresponds to a unique combination of 'customer_id', 'sensor_id', 'timestamp', and 'value'.

    Parameters:
    data (list): A list of dictionaries containing 'customer_id', 'sensor_id', 'timestamps', and 'values'.

    Returns:
    pandas DataFrame: A pandas DataFrame with the 'timestamps' and 'values' arrays flattened into rows.
    """
    
    # flatten the arrays
    flattened_data = []
    for item in data:
        timestamps_values = list(zip(item['timestamps'], item['values']))
        for timestamp, value in timestamps_values:
            flattened_data.append({
                'customer_id': item['customer_id'],
                'sensor_id': item['sensor_id'],
                'timestamp': timestamp,
                'value': value
            })

    # convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(flattened_data)
    
    return df