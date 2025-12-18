"""
QUESTION:
Design a function `sort_hashtable_by_values` that takes a dictionary (hashtable) as input, where keys are integers and values are strings, and returns a new dictionary with the same key-value pairs sorted in descending order by value. The function should be optimized to handle up to 1 million key-value pairs efficiently.
"""

def sort_hashtable_by_values(hashtable):
    # Convert hashtable to a list of key-value pairs
    items = list(hashtable.items())
    
    # Sort the list based on values in descending order
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    
    # Convert the sorted list back to a hashtable
    sorted_hashtable = {k: v for k, v in sorted_items}
    
    return sorted_hashtable