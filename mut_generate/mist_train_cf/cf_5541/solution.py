"""
QUESTION:
Write a function named `delete_element` that takes a list `lst` and an integer `element` as input. The function should delete the `element` from the list if it exists at least once, keeping track of the number of times the element was deleted. If the element is not found in the list, the list should remain unchanged. The function should return the modified list and the deletion count. The function should not use any built-in functions or methods to perform the deletion operation, and it should be able to handle cases where the element to be deleted is a negative number.
"""

def delete_element(lst, element):
    deletion_count = 0
    i = 0
    
    while i < len(lst):
        if lst[i] == element:
            del lst[i]
            deletion_count += 1
        else:
            i += 1
    
    return lst, deletion_count