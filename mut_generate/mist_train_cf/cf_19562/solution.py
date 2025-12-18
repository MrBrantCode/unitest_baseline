"""
QUESTION:
Create a function called "swap_list_elements" that takes a list and two indices as input, swaps the list elements at the specified indices, and returns the modified list. The function should handle duplicate elements, validate that the list is not empty and the indices are valid integers within the range of the list, and raise a custom exception for any failed validations.
"""

class SwapListElementsException(Exception):
    pass

def swap_list_elements(my_list, index1, index2):
    if not my_list:
        raise SwapListElementsException("List should not be empty.")
    
    if not isinstance(index1, int) or not isinstance(index2, int):
        raise SwapListElementsException("Indices should be valid integers.")
    
    if index1 < 0 or index1 >= len(my_list) or index2 < 0 or index2 >= len(my_list):
        raise SwapListElementsException("Indices should be within the range of the list.")
    
    if index1 == index2:
        if my_list.count(my_list[index1]) > 1:
            index2 = my_list.index(my_list[index1], index1 + 1)
        else:
            raise SwapListElementsException("Indices are the same and list does not contain duplicate elements.")
    
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list