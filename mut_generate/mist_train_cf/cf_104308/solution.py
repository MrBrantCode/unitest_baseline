"""
QUESTION:
Write a function called `insert_element` that takes in two parameters: 
- `lst`, a sorted list of integers in ascending order with a length between 0 and 1000
- `element`, an integer value between 0 and 1000 

The function should return a new list with the element inserted at the correct position, while still maintaining the ascending order of the list. If the element already exists in the list, it should be inserted after the last occurrence of the element.
"""

def insert_element(lst, element):
    """
    Inserts an element into a sorted list while maintaining the ascending order.

    Args:
        lst (list): A sorted list of integers in ascending order.
        element (int): The element to be inserted into the list.

    Returns:
        list: A new list with the element inserted at the correct position.
    """
    index = 0
    for i in range(len(lst)):
        if lst[i] > element:
            break
        index = i + 1
    
    last_index = None
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == element:
            last_index = i
            break
    
    if last_index is not None:
        lst.insert(last_index+1, element)
    else:
        lst.insert(index, element)
    
    return lst