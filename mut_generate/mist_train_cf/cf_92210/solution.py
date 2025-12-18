"""
QUESTION:
Create a function named `swap_elements` that takes a list `my_list` and two integers `index1` and `index2` as parameters. The function should swap the values of the list elements at `index1` and `index2` and return the modified list. If `index1` or `index2` is out of range, the function should raise a custom `IndexOutOfRangeException` with the error message "Indices are out of range." If the list is empty or `index1` and `index2` are not integers, the function should raise a custom `InvalidInputException` with the error message "Input list cannot be empty." or "Indices must be valid integers.", respectively.
"""

class IndexOutOfRangeException(Exception):
    pass

class InvalidInputException(Exception):
    pass

def swap_elements(my_list, index1, index2):
    # Validate input
    if not isinstance(my_list, list) or len(my_list) == 0:
        raise InvalidInputException("Input list cannot be empty.")
    if not isinstance(index1, int) or not isinstance(index2, int):
        raise InvalidInputException("Indices must be valid integers.")

    # Check if indices are out of range
    if index1 < 0 or index1 >= len(my_list) or index2 < 0 or index2 >= len(my_list):
        raise IndexOutOfRangeException("Indices are out of range.")

    # Swap elements
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    # Return modified list
    return my_list