"""
QUESTION:
Write a function `insert_between_elements` that inserts a new element between two specific elements in a list using a for loop, updating the indices of the following elements accordingly. The function should not increase the list's size before adding the new element.
"""

def insert_between_elements(my_list, target_value, new_element):
    """
    Inserts a new element between two specific elements in a list using a for loop, 
    updating the indices of the following elements accordingly.

    Args:
    my_list (list): The input list.
    target_value (int): The target value that the new element will be inserted between.
    new_element (int): The new element to be inserted.

    Returns:
    list: The updated list with the new element inserted.
    """
    for i in range(len(my_list)-1):
        if my_list[i] < target_value and my_list[i+1] > target_value:
            my_list.insert(i+1, new_element)
    return my_list