"""
QUESTION:
Create a function `sort_dict_array` that takes an array of dictionaries as input and returns a new sorted array. The sorting should be done in descending order by the value of 'popularity'. Additionally, dictionaries with a 'popularity' value of less than 3 should be placed at the end of the sorted array.
"""

def sort_dict_array(array):
    """
    Sorts an array of dictionaries by the value of 'popularity' in descending order.
    Dictionaries with a 'popularity' value of less than 3 are placed at the end of the sorted array.

    Args:
        array (list): A list of dictionaries.

    Returns:
        list: A sorted list of dictionaries.
    """
    return sorted(array, key=lambda x: (x['popularity'] >= 3, x['popularity']), reverse=True)