"""
QUESTION:
Write a function `add_item_to_list` that adds an item to a given list while adhering to the following rules:

- The function should not add the item if it already exists in the list and return an error message instead.
- The function should not add the item if it is not of the same data type as the existing items in the list and return an error message instead.
- The function should not add the item if the list has reached its maximum capacity and return an error message instead.
- The function can add the item at a specified position in the list (using an index) or at the end of the list if no index is provided.
- The function should return the updated list after adding the item.
"""

def add_item_to_list(item, my_list, max_capacity, index=None):
    # Check if the item already exists in the list
    if item in my_list:
        return "Item already exists in the list. Cannot add."

    # Check if the item is of the correct data type
    if my_list and not isinstance(item, type(my_list[0])):
        return "Incorrect data type. Cannot add."

    # Check if the list has reached its maximum capacity
    if len(my_list) >= max_capacity:
        return "List has reached its maximum capacity. Cannot add."

    # Add the item at the specified index or at the end of the list
    if index is None:
        my_list.append(item)
    else:
        my_list.insert(index, item)

    return my_list