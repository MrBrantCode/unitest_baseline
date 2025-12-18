"""
QUESTION:
Create a function named `sort_hashtable` that takes a dictionary (hashtable) as input and returns a new dictionary with its items sorted by their values in descending order. The function should not modify the original dictionary and should work for any given dictionary.
"""

def sort_hashtable(hashtable):
    """
    Returns a new dictionary with its items sorted by their values in descending order.

    Args:
        hashtable (dict): The input dictionary.

    Returns:
        dict: A new dictionary with sorted items.
    """
    return {k: v for k, v in sorted(hashtable.items(), key=lambda item: item[1], reverse=True)}