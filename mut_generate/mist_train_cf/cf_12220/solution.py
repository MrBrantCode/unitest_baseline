"""
QUESTION:
Create a function named `swap_elements` that takes a list and two indices as input, swaps the values at the given indices in the list, and returns the modified list. The function must handle cases when the indices are out of range by raising an `IndexOutOfRangeException` with the message "Indices are out of range." It should also validate the input to ensure the list is not empty and the indices are valid integers, raising an `InvalidInputException` with the message "Input list cannot be empty." or "Indices must be valid integers." if the validations fail.
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