"""
QUESTION:
Implement a function named `count_items` that takes a dictionary (hashmap) as input and returns the number of key-value pairs in the dictionary without using any built-in functions or methods for counting.
"""

def count_items(hashmap):
    """
    This function takes a dictionary as input and returns the number of key-value pairs.
    
    Parameters:
    hashmap (dict): The input dictionary.
    
    Returns:
    int: The number of key-value pairs in the dictionary.
    """
    count = 0
    for key, value in hashmap.items():
        count += 1
    return count