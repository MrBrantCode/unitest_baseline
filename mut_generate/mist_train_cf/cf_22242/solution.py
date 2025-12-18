"""
QUESTION:
Write a function `count_items` that takes a dictionary as input and returns the total number of items in the dictionary, including items in any nested dictionaries and lists. The function should recursively count items at all levels of nesting. The dictionary may contain any combination of primitive values, dictionaries, and lists, which can also be nested within each other.
"""

def count_items(data):
    count = 0
    if isinstance(data, dict):
        for key, value in data.items():
            count += 1 
            count += count_items(value) 
    elif isinstance(data, list):
        for item in data:
            count += 1 
            if isinstance(item, (dict, list)):
                count += count_items(item) 
    return count