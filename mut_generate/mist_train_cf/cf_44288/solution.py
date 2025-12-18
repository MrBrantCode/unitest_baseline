"""
QUESTION:
Create a function named `set_excel_column_width` that sets the width of all columns in an Excel file to a specified width. The function should take two parameters: `num_columns` (the number of columns in the Excel file) and `width` (the desired width of each column). The function should return a string representing the column range (e.g., "A:G") that can be used with the `set_column` method of the `ExcelWriter` class from the `pandas` library. The function should work for up to 26 columns.
"""

import string

def set_excel_column_width(num_columns, width):
    """
    Sets the width of all columns in an Excel file to a specified width.

    Args:
        num_columns (int): The number of columns in the Excel file.
        width (int): The desired width of each column.

    Returns:
        str: A string representing the column range (e.g., "A:G") that can be used with the set_column method of the ExcelWriter class from the pandas library.
    """
    last_column_letter = string.ascii_uppercase[num_columns - 1]
    return f"A:{last_column_letter}"