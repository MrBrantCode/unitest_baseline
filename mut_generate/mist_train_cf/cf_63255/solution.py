"""
QUESTION:
Create a function named `init_dataframe` that constructs a Pandas DataFrame from a given list of tuples, where each tuple consists of an integer and a dictionary. The dictionary should be unpacked into separate columns in the resulting DataFrame, with the integer serving as the row index or a separate column. The function should efficiently create the DataFrame without using loops and include checks for the length and type of the resulting DataFrame to ensure data integrity.
"""

import pandas as pd

def init_dataframe(data):
    ids = [d[0] for d in data]
    fruits = [d[1]['fruit'] for d in data]

    dataframe = pd.DataFrame({
        "id": ids,
        "fruit": fruits
    })
    
    return dataframe