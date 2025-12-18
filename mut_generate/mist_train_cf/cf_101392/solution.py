"""
QUESTION:
Implement a function named `sort_table` that takes a table and a list of column names as input, and returns the table sorted by the specified columns in ascending order. The function should also have an optional parameter that allows sorting the 'Integer Column' in descending order while keeping other columns in ascending order.
"""

def sort_table(table, columns, sort_integer_descending=False):
    """
    Sorts a table based on the given column names in ascending order. 
    If sort_integer_descending is True, the 'Integer Column' is sorted in descending order while keeping other columns in ascending order.
    """
    for column in columns:
        if column == 'Integer Column' and sort_integer_descending:
            table = sorted(table, key=lambda row: (-int(row[column]), row))
        else:
            table = sorted(table, key=lambda row: row[column])
    return table