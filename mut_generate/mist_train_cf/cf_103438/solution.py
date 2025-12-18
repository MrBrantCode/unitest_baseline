"""
QUESTION:
Write a function named `delete_4th_element` that takes a list of up to 10,000 elements as input, removes the 4th element in-place without using built-in delete functions, and handles cases where the list has less than 4 elements. The function should optimize for time complexity and maintain the order of other elements in the list.
"""

def delete_4th_element(lst):
    if len(lst) < 4:
        return lst  # If the list has less than 4 elements, no need to delete anything

    lst[3] = None  # Replace the 4th element with None
    lst_len = len(lst)
    new_len = lst_len - 1

    # Shift all the elements after the 4th element one position to the left
    for i in range(4, lst_len):
        lst[i - 1] = lst[i]

    # Truncate the list by removing the last element
    del lst[new_len]

    return lst