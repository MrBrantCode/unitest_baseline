"""
QUESTION:
Write a function named `check_same_data_type` that checks if all items in a list are of the same data type, including nested lists and dictionaries. The function should return `True` if all items are of the same data type and `False` otherwise. The function should aim for an optimal time complexity solution.
"""

def check_same_data_type(lst):
    if len(lst) < 2:
        return True

    first_type = type(lst[0])

    if first_type == list or first_type == dict:
        first_type = check_same_data_type(lst[0])

    for item in lst[1:]:
        item_type = type(item)
        if item_type == list or item_type == dict:
            item_type = check_same_data_type(item)
        
        if item_type != first_type:
            return False
    
    return True