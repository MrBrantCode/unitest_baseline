"""
QUESTION:
Write a function `add_item_to_list(lst, item, index=None, max_capacity=None)` that adds an item to the given list. The function should first check if the item already exists in the list. If it does, return an error message. Then, check if the item is of the same data type as the existing elements in the list. If not, return an error message. Next, check if the list has reached its maximum capacity. If it has, return an error message. If no issues are found, add the item at the specified index or at the end of the list if no index is provided, and return the updated list. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def add_item_to_list(lst, item, index=None, max_capacity=None):
    # Check if the item already exists in the list
    if item in lst:
        return "Item already exists in the list."

    # Check if the item is of the correct data type
    if len(lst) > 0 and not isinstance(item, type(lst[0])):
        return "Item is not of the correct data type."

    # Check if the list has reached its maximum capacity
    if max_capacity is not None and len(lst) >= max_capacity:
        return "List has reached its maximum capacity."

    # Add the item at the specified index or at the end of the list
    if index is not None:
        lst.insert(index, item)
    else:
        lst.append(item)

    return lst