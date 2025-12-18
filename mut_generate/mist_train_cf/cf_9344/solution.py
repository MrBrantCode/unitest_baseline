"""
QUESTION:
Implement a function named `custom_pop()` that takes a list (`lst`) and an optional index parameter (`index` with default value `-1`) and removes the element at the specified index from the list. The function should handle negative indexing and return the popped element without using the built-in `pop()` function or slicing.
"""

def entance(lst, index=-1):
    if index < 0:
        index += len(lst)
    
    popped_element = lst[index]
    lst[index:index + 1] = []
    
    return popped_element