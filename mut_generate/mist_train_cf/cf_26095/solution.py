"""
QUESTION:
Create a function named `searchArray` that takes in an array of objects `arr`, a key `key`, and a value `value` as parameters. The function should return the first object in the array where the object's key matches the given key and its corresponding value matches the given value.
"""

def searchArray(arr, key, value):
    """
    Search an array of objects by any parameter.

    Args:
    arr (list): A list of dictionaries.
    key (str): The key to be searched in the dictionaries.
    value (any): The value to be matched with the key.

    Returns:
    dict: The first dictionary where the key matches the given key and its corresponding value matches the given value.
    """
    return next((obj for obj in arr if obj.get(key) == value), None)