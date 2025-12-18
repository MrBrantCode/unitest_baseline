"""
QUESTION:
Write a function named `select_columns` that takes three parameters: a 2D list `data_table` representing a data table, a list `columns` specifying the columns to select, and an optional tuple `condition` specifying a condition to filter rows. The `condition` tuple should contain a column name and a value to match. The function should return a new 2D list containing the selected columns and filtered rows. If the specified column does not exist in the data table or the condition does not match any rows, the function should return an error message. The function should also check if the specified value in the condition is of the same data type as the values in the specified column and provide an error message if not. The time complexity of the function should be O(n), where n is the number of rows in the data table.
"""

def select_columns(data_table, columns, condition=None):
    # Check if the specified columns exist in the data table
    for col in columns:
        if col not in data_table[0]:
            return "Error: Column '{}' does not exist in the data table.".format(col)
    
    # Check if the condition is provided and valid
    if condition:
        column, value = condition
        if column not in data_table[0]:
            return "Error: Column '{}' does not exist in the data table.".format(column)
        if not all(isinstance(row[data_table[0].index(column)], type(value)) for row in data_table[1:]):
            return "Error: Specified value in the condition is not of the same data type as the values in the specified column."
    
    # Select the specified columns and filter rows based on the condition
    selected_table = []
    selected_table.append([col for col in data_table[0] if col in columns])
    
    for row in data_table[1:]:
        if not condition or row[data_table[0].index(column)] == value:
            selected_row = [row[data_table[0].index(col)] for col in columns]
            selected_table.append(selected_row)
    
    # Check if the condition does not match any rows in the data table
    if condition and len(selected_table) == 1:
        return "No rows match the specified condition."
    
    return selected_table