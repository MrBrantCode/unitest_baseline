"""
QUESTION:
Create a function called `insert_item` that takes two parameters: `existing_list` and `new_item`. The function should insert `new_item` into `existing_list` at the correct position to maintain the list in ascending order. If `existing_list` contains duplicate elements, `new_item` should be inserted after the last occurrence of any duplicate element. The function must return the updated list.
"""

def insert_item(existing_list, new_item):
    """
    Inserts new_item into existing_list at the correct position to maintain the list in ascending order.
    
    Args:
    existing_list (list): The list into which the new item will be inserted.
    new_item: The item to be inserted into the list.
    
    Returns:
    list: The updated list with the new item inserted.
    """
    index = len(existing_list)
    
    for i in range(len(existing_list)-1, -1, -1):
        if existing_list[i] <= new_item:
            index = i + 1
            break
    
    existing_list.insert(index, new_item)
    return existing_list