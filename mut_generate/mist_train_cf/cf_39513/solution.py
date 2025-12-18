"""
QUESTION:
Implement a function `getFieldsSchema(data)` that takes a dataset as input, where the dataset can be a dictionary or a pandas DataFrame, and returns a dictionary representing the schema of the fields in the dataset, including their names and data types. The function should support various data types such as string, integer, float, and date.
"""

import pandas as pd

def getFieldsSchema(data):
    if isinstance(data, dict):
        df = pd.DataFrame(data)
        schema = df.dtypes.to_dict()
        return schema
    elif isinstance(data, pd.DataFrame):
        schema = data.dtypes.to_dict()
        return schema
    else:
        return "Invalid data format"