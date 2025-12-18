"""
QUESTION:
Implement a function named `join_tables` that combines rows from two tables based on a related column between them. The function should take two tables as input, where each table is represented as a dictionary with column names as keys and lists of values as values. The function should return a list of joined rows, where each row is a list of values from the two tables that have matching 'id' values.

Restrictions:

- The function should have a time complexity of O(n^2), where n is the total number of rows in both tables combined.
- The function should have a space complexity of O(n), where n is the total number of rows in both tables combined.
"""

def join_tables(table1, table2):
    """
    Combines rows from two tables based on a related column between them.

    Args:
        table1 (dict): The first table with column names as keys and lists of values as values.
        table2 (dict): The second table with column names as keys and lists of values as values.

    Returns:
        list: A list of joined rows, where each row is a list of values from the two tables that have matching 'id' values.
    """
    result = []
    for i, id1 in enumerate(table1['id']):
        for j, id2 in enumerate(table2['id']):
            if id1 == id2:
                row1 = [value[i] for value in table1.values()]
                row2 = [value[j] for value in table2.values()]
                result.append(row1 + row2)
    return result