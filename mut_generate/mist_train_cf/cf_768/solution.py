"""
QUESTION:
Write a function named `custom_sort` that sorts a list of dictionaries based on multiple key values with different sorting orders for each key. The function should take two parameters: a list of dictionaries `data` and a list of tuples `sort_keys` where each tuple contains the key and the sorting order (either 'asc' for ascending or 'desc' for descending).
"""

def custom_sort(data, sort_keys):
    return sorted(data, key=lambda x: tuple(x[key] if order == 'asc' else -x[key] for key, order in sort_keys))