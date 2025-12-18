"""
QUESTION:
Design a function `sort_hashtable_by_values` that takes a dictionary (hashtable) with integer keys and string values as input, and returns a new dictionary sorted by its values in descending order. The function should be optimized for time complexity to handle up to 1 million key-value pairs.
"""

def sort_hashtable_by_values(hashtable):
    # Convert hashtable to a list of key-value pairs
    items = list(hashtable.items())
    
    # Sort the list based on values in descending order
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    
    # Convert the sorted list back to a hashtable
    sorted_hashtable = {k: v for k, v in sorted_items}
    
    return sorted_hashtable