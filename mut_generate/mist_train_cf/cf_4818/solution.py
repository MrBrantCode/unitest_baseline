"""
QUESTION:
Remove an element from a list at the specified index in-place with a time complexity of O(n). The function should modify the original list without creating a new one and not use any built-in removal functions or methods, except for length and indexing. 

Function name: remove_element_at_index(lst, index) 
Input: lst - a list of integers, index - the index of the element to be removed.
"""

def remove_element_at_index(lst, index):
    length = len(lst)
    if index >= length:
        return lst
    
    for i in range(index, length - 1):
        lst[i] = lst[i+1]
    
    lst.pop()
    return lst