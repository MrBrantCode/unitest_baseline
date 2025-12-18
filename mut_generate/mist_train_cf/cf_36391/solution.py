"""
QUESTION:
Implement the `text_table` function to generate a text table from given data, row and column dimensions, and a function to calculate cell values. The function should be able to handle multi-character separators for both rows and columns.

The function `text_table` takes in the following parameters:
- `data`: A list of dictionaries, where each dictionary represents a row of the table. Each dictionary contains key-value pairs representing the column names and their corresponding values.
- `dim_rows`: A list of strings representing the dimension names for the rows.
- `dim_cols`: A list of strings representing the dimension names for the columns.
- `value_func`: A function that takes a list of dictionaries as input and returns a single value. This function is used to calculate the value for each cell in the table.
- `d_cols`: A string representing the separator between columns. Default value is a single space.
- `d_rows`: A string representing the separator between rows. Default value is a newline character.

The function should return a string representing the text table, formatted with the specified row and column separators, and the cell values calculated using the provided `value_func`.
"""

from typing import List, Dict, Any, Callable

def text_table(data: List[Dict[str, Any]], dim_rows: List[str], dim_cols: List[str], value_func: Callable[[List[Dict[str, Any]]], Any], d_cols: str = " ", d_rows: str = "\n") -> str:
    table = []

    # Create the header row
    header = d_cols.join(dim_cols)
    table.append(header)

    # Create the data rows
    for row_name, row_data in zip(dim_rows, data):
        row_values = [str(value_func([row_data]))]
        for col_name in dim_cols[1:]:
            row_values.append(str(value_func([row_data])))
        table.append(row_name + d_cols + d_cols.join(row_values))

    return d_rows.join(table)