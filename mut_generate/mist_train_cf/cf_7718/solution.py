"""
QUESTION:
Write a function named `count_items` that takes a dictionary as input. The dictionary can have up to 10^6 key-value pairs, up to 10 levels of nesting, and its lists can have up to 10^4 elements. The function should return the total count of items in the dictionary, including items in nested dictionaries and lists.
"""

def count_items(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, dict):
            count += count_items(value)  # recursively count items in nested dictionary
        elif isinstance(value, list):
            count += len(value)  # count items in list
            for item in value:
                if isinstance(item, dict):
                    count += count_items(item)  # recursively count items in nested dictionary within list
        else:
            count += 1  # count item in top-level dictionary
    return count