"""
QUESTION:
Write a function `add_item_to_list(lst, item, index=None)` that adds an item to a given list while adhering to the following restrictions:
- The item must not already exist in the list.
- The item must be of type `int`.
- The list must not have reached its maximum capacity of 10 elements.
- If an index is specified, it must be within the valid range of the list.
- If no index is specified, the item should be added at the end of the list.
- The function must have a time complexity of O(n) and a space complexity of O(1).
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