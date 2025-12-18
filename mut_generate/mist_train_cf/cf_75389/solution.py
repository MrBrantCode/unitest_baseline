"""
QUESTION:
Create a function named 'mergeAndSortLists' that merges two integer lists and sorts the combined list. The function should take three arguments: two integer lists and an order parameter ('asc' or 'desc'). It should validate if all elements in the lists are integers and handle any exceptions. If an invalid element is found, it should print a message "Invalid element(s) found in list(s), combined and sorted list cannot be produced." The function should also be able to be implemented in a single line of code.
"""

def mergeAndSortLists(list1, list2, order): 
    return sorted(list1 + list2, reverse = True if order == 'desc' else False) if all(isinstance(i, int) for i in list1 + list2) else print("Invalid element(s) found in list(s), combined and sorted list cannot be produced.")