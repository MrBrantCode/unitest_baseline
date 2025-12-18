"""
QUESTION:
Define a function `total_earned` that takes a row of a DataFrame as input and returns the product of the `quantity_sold` and `unit_price` columns. Define another function `calculate_total_earned` that takes a DataFrame `df` with columns `product_id`, `quantity_sold`, and `unit_price`, and adds a new column `total_earned` to the DataFrame by applying the `total_earned` function to each row. The function should modify the input DataFrame and return the modified DataFrame.
"""

import pandas as pd

def total_earned(row):
    return row['quantity_sold'] * row['unit_price']

def total_earned_func(df):
    df['total_earned'] = df.apply(total_earned, axis=1)
    return df