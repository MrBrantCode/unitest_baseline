"""
QUESTION:
Write a function named `sort_hashtable_by_value` that takes a dictionary as input and returns a new dictionary sorted by its values in descending order. The function should not modify the original dictionary and should work with any dictionary containing hashable keys and comparable values.
"""

def sort_hashtable_by_value(hashtable):
    """
    Returns a new dictionary sorted by its values in descending order.

    Args:
        hashtable (dict): The input dictionary.

    Returns:
        dict: A new dictionary sorted by its values in descending order.
    """
    return {k: v for k, v in sorted(hashtable.items(), key=lambda item: item[1], reverse=True)}