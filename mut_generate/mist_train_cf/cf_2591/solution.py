"""
QUESTION:
Write a function called `insert_element` that takes a sorted list of integers `lst` and an integer value `element` as input. The function should return a new list with the `element` inserted at the correct position, maintaining the ascending order of the list. If the `element` already exists in the list, it should be inserted before the first occurrence of the `element`. The input list `lst` has a length between 0 and 1000 (inclusive), and the `element` is an integer between 0 and 1000 (inclusive).
"""

def insert_element(lst, element):
    """
    Inserts an element into a sorted list while maintaining the ascending order.
    
    Args:
        lst (list): A sorted list of integers.
        element (int): The integer value to be inserted.
    
    Returns:
        list: A new list with the element inserted at the correct position.
    """
    
    # Create a copy of the list
    new_list = lst.copy()
    
    # Try to find the index of the first occurrence of the element in the list
    try:
        index = new_list.index(element)
    except ValueError:
        # If the element is not found, set the index to the length of the list
        index = len(new_list)
    
    # Insert the element at the index
    new_list.insert(index, element)
    
    # Return the modified list
    return new_list