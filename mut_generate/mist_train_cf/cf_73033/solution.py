"""
QUESTION:
Implement a function called `server_side_pagination` that takes in a database table, column name, sort order, page size, and page number as inputs, and returns the pertinent data from the database without bringing the entire table to the client. The function should support filtering based on a given condition.
"""

def server_side_pagination(table, column_name, sort_order, page_size, page_number, condition=None):
    """
    This function implements server-side pagination, filtering and sorting.
    
    Args:
        table (list): A list of dictionaries representing the database table.
        column_name (str): The name of the column to sort by.
        sort_order (str): The order of sorting. Either 'asc' or 'desc'.
        page_size (int): The number of records per page.
        page_number (int): The current page number.
        condition (function, optional): A function that takes a dictionary and returns a boolean. Defaults to None.

    Returns:
        list: A list of dictionaries representing the pertinent data from the database.
    """
    
    # First, we filter the data if a condition is provided
    if condition is not None:
        data = [row for row in table if condition(row)]
    else:
        data = table
    
    # Then, we sort the data based on the given column and sort order
    if sort_order == 'asc':
        data.sort(key=lambda x: x[column_name])
    elif sort_order == 'desc':
        data.sort(key=lambda x: x[column_name], reverse=True)
    
    # Finally, we paginate the data
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return data[start_index:end_index]