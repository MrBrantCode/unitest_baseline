"""
QUESTION:
Create a function named `process_movement_data` that takes a Pandas dataframe `Movement_Data` as input and returns a list of dictionaries. Each dictionary should contain the non-acceleration and non-orientation key-value pairs from each reading in the dataframe. The function should exclude the 'Acceleration' and 'Orientation' key-value pairs from each reading and return the remaining key-value pairs. The input dataframe `Movement_Data` is expected to have a dictionary of readings as its values.
"""

import pandas as pd
from typing import List, Dict, Any

def process_movement_data(Movement_Data: pd.DataFrame) -> List[Dict[str, Any]]:
    result = []
    for reading in Movement_Data:
        data = Movement_Data[reading]
        filtered_data = {key: value for key, value in data.items() if key not in ['Acceleration', 'Orientation']}
        result.append(filtered_data)
    return result