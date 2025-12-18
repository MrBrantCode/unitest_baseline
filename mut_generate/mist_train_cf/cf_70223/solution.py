"""
QUESTION:
Create a function named `manipulate_dataframe` that takes a pandas DataFrame and a dictionary of data manipulation directives as input. The dictionary may contain the following directives: 'rename_columns', 'drop_columns', and 'change_dtype'. The function should apply these directives to the DataFrame, handling edge cases where specified columns do not exist. The function should return the modified DataFrame.
"""

import pandas as pd

def manipulate_dataframe(df: pd.DataFrame, directives: dict) -> pd.DataFrame:

    for operation, instruction in directives.items():
        if operation == 'rename_columns':
            for old_name, new_name in instruction.items():
                if old_name in df.columns:
                    df = df.rename(columns={old_name: new_name})
                else:
                    print(f"Could not find column {old_name} to rename")

        elif operation == 'drop_columns':
            for column in instruction:
                if column in df.columns:
                    df = df.drop(column, axis=1)               
                else:
                    print(f"Could not find column {column} to drop")

        elif operation == 'change_dtype':
            for column, dtype in instruction.items():
                if column in df.columns:
                    df[column] = df[column].astype(dtype)
                else:
                    print(f"Could not find column {column} for changing data type")

    return df