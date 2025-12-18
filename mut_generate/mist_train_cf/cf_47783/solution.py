"""
QUESTION:
Write a function `is_valid(record)` that takes a pandas DataFrame record as input and checks for validity based on the following conditions: 
- The record should not have any missing values.
- The 'vehicle' and 'color' columns should be strings.
- The 'price' column should be a positive number.

Additionally, write code to apply this function to each record in a DataFrame, create a report of invalid records, and calculate the count of unique values in the 'vehicle' and 'color' columns for the valid records.

The input DataFrame may contain missing values (None or NaN) and erroneous data types or values, such as non-string entries in 'vehicle' and 'color' columns, and negative or non-numeric values in 'price'.
"""

import pandas as pd
import numpy as np

def entrance(record):
    if record.vehicle is None or record.color is None or record.price is None:
        return 'Record Invalid: Missing Values'
    if not isinstance(record.vehicle, str):
        return 'Record Invalid: Vehicle must be string'
    if not isinstance(record.color, str):
        return 'Record Invalid: Color must be string'
    if isinstance(record.price, str) or record.price < 0:
        return 'Record Invalid: Price must be a positive number'
    return 'Record Valid'