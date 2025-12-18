"""
QUESTION:
Design a function `should_index_column` that determines whether indexing a column in a database table is beneficial or not. The function should take the following parameters: `table_size`, the number of records in the table, and `query_type`, a string indicating the type of queries performed on the table ('sequential_scan', 'full_table_scan', or 'random_queries'). The function should return `True` if indexing the column is beneficial and `False` otherwise. Assume that the data in the table is not updated frequently.
"""

def should_index_column(table_size, query_type):
    """
    Determines whether indexing a column in a database table is beneficial or not.

    Args:
        table_size (int): The number of records in the table.
        query_type (str): The type of queries performed on the table ('sequential_scan', 'full_table_scan', or 'random_queries').

    Returns:
        bool: True if indexing the column is beneficial, False otherwise.
    """
    if table_size < 1000:
        # For small tables, indexing may not be beneficial due to the overhead of maintaining the index.
        return False
    elif query_type in ['sequential_scan', 'full_table_scan']:
        # Indexing may not provide significant advantages for sequential scans or full table scans.
        return False
    else:
        # For large tables with random queries, indexing can significantly improve query performance.
        return True