"""
QUESTION:
Create a function called `swap_list_elements` that takes a list `my_list` and two integers `index1` and `index2`. The function should swap the values of the list elements at the specified indices and return the modified list. 

The function should handle the case when the list contains duplicate elements and the specified indices are the same by swapping the values of the elements once. The function should also validate the input by checking that the list is not empty, the indices are valid integers, and the indices are within the range of the list. If any of these validations fail, the function should raise a custom exception with an appropriate error message.
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