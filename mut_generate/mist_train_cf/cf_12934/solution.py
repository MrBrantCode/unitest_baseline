"""
QUESTION:
Write a Python function called `perform_join_operation` that takes in two lists of dictionaries, `table1` and `table2`, and a common key `key`. The function should return a list of dictionaries where each dictionary contains the joined data from `table1` and `table2` based on the provided `key`. The function should only include rows where the values of the common key match between the two tables.
"""

def perform_join_operation(table1, table2, key):
    """
    This function performs an inner join operation between two lists of dictionaries.
    
    Args:
        table1 (list): The first list of dictionaries.
        table2 (list): The second list of dictionaries.
        key (str): The common key to join on.
    
    Returns:
        list: A list of dictionaries containing the joined data.
    """
    return [{**row1, **row2} 
            for row1 in table1 
            for row2 in table2 
            if row1[key] == row2[key]]