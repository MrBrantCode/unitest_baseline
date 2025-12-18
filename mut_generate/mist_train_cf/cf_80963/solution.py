"""
QUESTION:
Create a function `remove_items` that removes instances of a set of specified items from multiple lists that contain various forms of data. The function should take a list or tuple of items to remove as its first argument and any number of lists as subsequent arguments. The function should return a list of lists with the specified items removed. If any of the specified items are not found in the lists, the function should return a message indicating this. The function should also handle cases where the specified items or the lists themselves do not exist, and should check for errors such as non-list arguments and non-string items to remove.
"""

def remove_items(items_to_remove, *lists):
    # Check if items_to_remove is a list or a tuple
    if not isinstance(items_to_remove, (list, tuple)):
        return 'Error: items_to_remove should be a list or a tuple.'
    
    # Check if each list to operate on is actually a list
    for lst in lists:
        if not isinstance(lst, list):
            return 'Error: All additional arguments should be of type list.'
    
    # Check if each item to remove is a string
    for item in items_to_remove:
        if not isinstance(item, str):
            return 'Error: All items to remove should be strings.'
    
    # Create a new list to hold the result
    result = []
    
    # Iterate over each list
    for lst in lists:
        # Filter the list to exclude items_to_remove and append it to result
        result.append([item for item in lst if item not in items_to_remove])

    # Check if any changes were made
    if sum(len(lst) for lst in lists) == sum(len(lst) for lst in result):
        return 'No specified items found in provided lists.'
        
    return result