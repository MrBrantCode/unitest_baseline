"""
QUESTION:
Write a function `clear_data` that takes a list of dictionaries as input, clears all the entries from the list, and returns the empty list. The input list represents a data set with columns "ID", "Title", and "Location", but the function should be able to clear any list of dictionaries, regardless of the column names.
"""

def clear_data(data):
    """
    Clears all entries from the input list of dictionaries.

    Args:
        data (list[dict]): The input list of dictionaries.

    Returns:
        list[dict]: The empty list.
    """
    data.clear()
    return data