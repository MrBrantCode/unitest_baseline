"""
QUESTION:
Implement a function called `count_hashmap_items` that takes a hashmap as input and returns the number of key-value pairs without using any built-in functions or methods for counting.
"""

def count_hashmap_items(hashmap):
    """
    Returns the number of key-value pairs in a hashmap.

    Args:
        hashmap (dict): The input hashmap.

    Returns:
        int: The number of key-value pairs in the hashmap.
    """
    count = 0
    for key, value in hashmap.items():
        count += 1
    return count