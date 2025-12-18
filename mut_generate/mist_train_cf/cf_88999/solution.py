"""
QUESTION:
Create a function `delete_element(lst, element)` that takes a list `lst` and an element as input, deletes all occurrences of the element from the list, and returns the modified list along with the count of deleted elements. The function should not use any built-in list deletion methods and should handle cases where the element to be deleted is a negative number. If the element is not found in the list, the original list should be returned along with a deletion count of 0.
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