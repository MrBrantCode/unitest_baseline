"""
QUESTION:
Create a function named create_dataframe that takes a list of tuples as input, where each tuple contains an integer and a dictionary with a 'fruit' key. The function should return a pandas DataFrame with two columns: 'Id' (integer) and 'Fruit' (string). The function must handle missing 'fruit' values in the dictionaries, log any exceptions during DataFrame creation, and ensure proper data types for the DataFrame columns. The input list of tuples can be of any size, and the function should be optimized for larger datasets.
"""

import pandas as pd
from typing import Tuple, List

def create_dataframe(data: List[Tuple[int, dict]]) -> pd.DataFrame:
    try:
        ids, fruit_dicts = zip(*data)
        fruits = [d.get('fruit', None) for d in fruit_dicts]
        df = pd.DataFrame({'Id': ids, 'Fruit': fruits})
        df['Id'] = df['Id'].astype(int)
        df['Fruit'] = df['Fruit'].astype(str)
        df['Fruit'].replace('None', 'Missing', inplace=True)
        return df

    except Exception as e:
        print(f"Exception occurred: {e}")
        return None