"""
QUESTION:
Write a Python function `calculate_list_size` that calculates the number of rows `x` in a contiguous list of non-blank cells within a single column in a spreadsheet. The function should take as input a list of column values. The list is guaranteed to be contiguous with no gaps above, below, or beside it, and there are no other non-empty cells in the column outside of the list.
"""

def calculate_list_size(column_values):
    """
    Calculate the number of rows in a contiguous list of non-blank cells within a single column in a spreadsheet.

    Args:
        column_values (list): A list of column values.

    Returns:
        int: The number of non-blank cells in the column.
    """
    return sum(1 for value in column_values if value is not None and value != '')