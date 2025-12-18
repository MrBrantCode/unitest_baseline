"""
QUESTION:
Create a function to optimize the search query on a text field that treats 'IJ' and 'Y' as interchangeable characters in a case-insensitive manner. The function should improve performance by minimizing the need for full table scans. Assume the database uses a case-insensitive collation and the input search string can contain either 'IJ' or 'Y'.
"""

def optimize_search_query(field1, search_string):
    """
    Optimizes the search query on a text field that treats 'IJ' and 'Y' as interchangeable characters in a case-insensitive manner.

    Args:
        field1 (str): The original text field.
        search_string (str): The input search string.

    Returns:
        bool: True if the search string is found in the field, False otherwise.
    """
    field1_replaced = field1.replace('Y', 'IJ').lower()
    search_string_replaced = search_string.replace('Y', 'IJ').lower()
    return search_string_replaced in field1_replaced