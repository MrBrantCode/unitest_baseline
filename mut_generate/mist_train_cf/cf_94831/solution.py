"""
QUESTION:
Write a function called `move_second_to_beginning` that takes a list of elements as input and rearranges the list to move the second-to-last element to the beginning. If the input list has less than 2 elements, return the list as is. The function should not use any built-in list manipulation methods or slicing operations.
"""

def move_second_to_beginning(lst):
    if len(lst) < 2:  # Check if the list has at least 2 elements
        return lst
    
    second_to_last = lst[-2]  # Get the second-to-last element
    
    # Shift all elements to the right by one position
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    
    lst[0] = second_to_last  # Place the second-to-last element at the beginning
    
    return lst