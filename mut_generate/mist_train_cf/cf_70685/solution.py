"""
QUESTION:
Create a function named `sort_data` that sorts a list of dictionaries by the "age" field in descending order. If two dictionaries have the same "age", they should be sorted based on the lexicographic order of their "name" in ascending order.
"""

def sort_data(data):
    """
    Sorts a list of dictionaries by the "age" field in descending order. 
    If two dictionaries have the same "age", they are sorted based on the lexicographic order of their "name" in ascending order.

    Args:
        data (list): A list of dictionaries containing "name" and "age" fields.

    Returns:
        list: A sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: (-x['age'], x['name']))