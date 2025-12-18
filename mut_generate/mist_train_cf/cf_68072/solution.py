"""
QUESTION:
Given a doubly linked list and a target node value, write a function `get_indices(dll, value)` that returns the indices of all nodes with the given value in the list. The function should not traverse the linked list from the head, and should be able to handle cases where the target value appears multiple times in the list.
"""

def get_indices(dll, value):
    if value in dll.dict:
        return dll.dict[value]  
    return []