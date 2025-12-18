"""
QUESTION:
Create a function named `sort_by_key` that takes a list of dictionaries as input and returns a new list where the dictionaries are sorted in ascending order based on their 'name' key value. The input list contains dictionaries with 'name' and 'age' keys, and each dictionary has a string value for 'name' and an integer value for 'age'. The function should not modify the original list.
"""

def sort_by_key(arr):
    """
    Sorts a list of dictionaries in ascending order based on their 'name' key value.

    Args:
    arr (list): A list of dictionaries with 'name' and 'age' keys.

    Returns:
    list: A new list of dictionaries sorted by the 'name' key value.
    """
    return sorted(arr, key=lambda i: i['name'])