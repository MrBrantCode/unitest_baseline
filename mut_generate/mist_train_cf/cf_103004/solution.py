"""
QUESTION:
Design a function named `search_list(lst, item)` that takes a list `lst` and an item as input, and returns the index of the first occurrence of the item in the list. If the item is not found in the list, the function should return -1. The function should be able to handle lists containing duplicate elements.
"""

def search_list(lst, item):
    # Initialize the index variable
    index = -1

    # Iterate through the list
    for i in range(len(lst)):
        # If the current element matches the specified item
        if lst[i] == item:
            # Update the index variable and break the loop
            index = i
            break
    
    # Return the index
    return index