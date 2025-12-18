"""
QUESTION:
Implement a function `build_log_hierarchy(df, relevant_columns)` to construct a hierarchical structure based on the log data from a given dataframe `df`. The `df` contains a column named `relevant_log_column` and multiple other columns. The `relevant_columns` parameter specifies the columns to be used for building the hierarchy. The function should return a dictionary where the keys are log templates derived from the `relevant_log_column` in lowercase and the values are lists of concatenated column name and value (in lowercase) separated by `#`, excluding empty values.
"""

import pandas as pd

def build_log_hierarchy(df, relevant_columns):
    log_hierarchy = {}
    for _, row in df.iterrows():
        log_template = str(row['relevant_log_column']).lower()
        for column in relevant_columns:
            row_value = (
                column + "#" + str(row[column]).lower()
                if len(str(row[column])) > 0
                else ""
            )
            if row_value:
                if log_template not in log_hierarchy:
                    log_hierarchy[log_template] = []
                log_hierarchy[log_template].append(row_value)
    return log_hierarchy