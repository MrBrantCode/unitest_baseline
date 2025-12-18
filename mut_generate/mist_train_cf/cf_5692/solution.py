"""
QUESTION:
Write a function `binary_search(dictionary, key)` that searches for a given `key` in a sorted dictionary and returns its corresponding value if found, using a binary search algorithm. The dictionary is sorted by its keys. The function should return `None` if the key is not found.
"""

def binary_search(dictionary, key):
    """
    Searches for a given key in a sorted dictionary and returns its corresponding value if found, 
    using a binary search algorithm. The dictionary is sorted by its keys.

    Args:
        dictionary (dict): A sorted dictionary.
        key: The key to be searched.

    Returns:
        The corresponding value if the key is found, otherwise None.
    """
    low = 0
    high = len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_key = list(dictionary.keys())[mid]

        if mid_key == key:
            return list(dictionary.values())[mid]
        elif mid_key < key:
            low = mid + 1
        else:
            high = mid - 1

    return None