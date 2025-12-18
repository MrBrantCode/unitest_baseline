"""
QUESTION:
Implement a function called `extract_and_split_subnets` that takes in a DataFrame `csv_table`, a list `relevant_subnets`, and a string `tablename` as inputs. The function should check if the input `csv_table` is a valid DataFrame and contains a column named "subnet". If these conditions are met, it should extract subnet information from the "subnet" column, split it into separate columns, and return the modified DataFrame. The function should also handle cases where no extraction is needed, such as when "complete_data" is present in `relevant_subnets` or when the input `csv_table` is empty.
"""

import pandas as pd
from copy import deepcopy

def extract_and_split_subnets(csv_table, relevant_subnets, tablename):
    # Ensure iterability of relevant_subnets[0] and obtain lv_subnets
    hv_subnets = relevant_subnets[0]
    lv_subnets = relevant_subnets[1]

    # Check if no extraction is needed
    if "complete_data" in hv_subnets or (isinstance(csv_table, pd.DataFrame) and csv_table.empty):
        return csv_table  # no extraction needed

    # Deep copy the csv_table to avoid modifying the original DataFrame
    csv_table = deepcopy(csv_table)

    # Check if csv_table is a DataFrame and "subnet" column exists
    if isinstance(csv_table, pd.DataFrame) and "subnet" in csv_table.columns:
        # Split the "subnet" column into separate columns
        subnet_split = csv_table.subnet.str.split("_", expand=True)
        # Assign the split columns to the original DataFrame
        csv_table[["subnet_prefix", "subnet_suffix"]] = subnet_split
        # Drop the original "subnet" column
        csv_table.drop(columns=["subnet"], inplace=True)
        return csv_table

    # Return the original csv_table if no extraction is performed
    return csv_table