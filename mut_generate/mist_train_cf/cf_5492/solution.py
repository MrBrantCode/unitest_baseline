"""
QUESTION:
Write a function named `add_item_to_list` that takes in a list, an item, and an optional index, and adds the item to the list at the specified index if it does not already exist in the list, is of the correct data type, and the list has not reached its maximum capacity of 10 elements. The function should return an error message if any of these conditions are not met, otherwise it should return the updated list. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def add_item_to_list(lst, item, index=None):
    # Check if item already exists in the list
    if item in lst:
        return "Item already exists in the list."
    
    # Check if item is of the correct data type
    if not isinstance(item, int):
        return "Item is not of the correct data type."
    
    # Check if list has reached its maximum capacity
    if len(lst) >= 10:
        return "List has reached its maximum capacity."
    
    # Check if index is valid
    if index is not None and (index < 0 or index > len(lst)):
        return "Invalid index specified."
    
    # Add item at the specified index or at the end of the list
    if index is None:
        lst.append(item)
    else:
        lst.insert(index, item)
    
    # Return the updated list
    return lst