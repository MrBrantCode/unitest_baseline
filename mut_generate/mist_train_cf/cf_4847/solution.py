"""
QUESTION:
Implement a function named `get_second_item` that can accept either a Dictionary or a List as an argument and returns the second item in the collection. The function should handle both nested Dictionaries and nested Lists, and return `None` if the collection has less than two items.
"""

def get_second_item(data):
    if isinstance(data, dict):  
        values = list(data.values())
        if len(values) >= 2:
            return values[1]
    elif isinstance(data, list):  
        if len(data) >= 2:
            return data[1]
    return None