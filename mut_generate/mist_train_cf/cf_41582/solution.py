"""
QUESTION:
Implement a function `process_financial_data` that takes a pandas DataFrame `data` and a list of strings `ignore_columns` as input. The DataFrame contains financial data with dates as column names and prices as values. The function should filter out the specified columns in `ignore_columns` and reformat the remaining data into a list of dictionaries containing date-price pairs for each record in the DataFrame. The function should return this list of dictionaries.
"""

import pandas as pd
from typing import List, Dict, Union

def process_financial_data(data: pd.DataFrame, ignore_columns: List[str]) -> List[Dict[str, Union[str, float]]]:
    list_res = data.to_dict(orient='records')  
    new_list_res = []
    for rec in list_res:
        all_keys = rec.keys()
        dates = [{'date': key, 'price': rec[key]} for key in all_keys if key not in ignore_columns]
        new_list_res.append(dates)  
    return new_list_res