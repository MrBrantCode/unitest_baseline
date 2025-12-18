"""
QUESTION:
Write a function named `select_columns` that takes a 2D list `data_table` and a list of column names `columns`. The function should return a new 2D list containing only the specified columns. Optionally, the function can take a tuple `condition` where the first element is a column name and the second element is a value. The function should then filter the rows based on the condition that the value in the specified column equals the given value. If the specified column does not exist in the data table, the function should return an error message. If the specified condition does not match any rows in the data table, the function should return an error message. If the specified value in the condition is not of the same data type as the values in the specified column, the function should return an error message. The function should have a time complexity of O(n), where n is the number of rows in the data table.
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