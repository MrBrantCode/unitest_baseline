"""
QUESTION:
Create a function named `sort_and_insert` that takes a list and a new element as input. The function should create a new list that includes the original list's elements and the new element, which must be inserted at the end of the list. The new list must be sorted in descending order.
"""

def sort_and_insert(original_list, new_element):
    """Creates a new list that includes the original list's elements and the new element, 
    sorted in descending order."""
    new_list = original_list.copy()
    new_list.append(new_element)
    new_list.sort(reverse=True)
    return new_list