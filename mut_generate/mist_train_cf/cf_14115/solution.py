"""
QUESTION:
Write a function named `select_columns` that takes a 2D list `table` representing a data table and three parameters: a list of column names `columns`, a column name `condition_column`, and a condition value `condition_value`. The function should return a new 2D list containing the selected columns from the original table, filtered by the condition if specified. The function should return `None` if any column name in `columns` or `condition_column` does not exist in the table. If the condition does not match any rows, the function should return an empty list. The function should have a time complexity of O(n), where n is the number of rows in the data table.
"""

def select_columns(table, columns, condition_column=None, condition_value=None):
    # Find the indices of the specified columns
    column_indices = []
    for column in columns:
        if column in table[0]:
            column_indices.append(table[0].index(column))
        else:
            return None

    # Filter rows based on the condition, if specified
    if condition_column and condition_column in table[0]:
        condition_index = table[0].index(condition_column)
        return [[row[column_index] for column_index in column_indices] for row in table[1:] if row[condition_index] == condition_value]
    else:
        return [[row[column_index] for column_index in column_indices] for row in table[1:]]