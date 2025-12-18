"""
QUESTION:
Write a function `sort_dict_list` that takes a list of dictionaries and a list of tuples, where each tuple contains a key from the dictionary and a sorting order (ascending or descending), and returns a new list of dictionaries sorted by the specified keys and orders. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_dict_list(dict_list, key_orders):
    """
    Sort a list of dictionaries based on the specified keys and orders.

    Args:
    dict_list (list): A list of dictionaries.
    key_orders (list): A list of tuples, where each tuple contains a key from the dictionary and a sorting order (ascending or descending).

    Returns:
    list: A new list of dictionaries sorted by the specified keys and orders.
    """
    def get_sort_key(x):
        sort_keys = []
        for key, order in key_orders:
            if order == 'ascending':
                sort_keys.append(x[key])
            elif order == 'descending':
                sort_keys.append(-x[key])
        return tuple(sort_keys)

    return sorted(dict_list, key=get_sort_key)