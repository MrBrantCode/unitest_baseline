"""
QUESTION:
Write a function `reverse_copy` that takes a list as input and returns a new list with the same elements in reverse order, without modifying the original list. The function should not use any built-in reverse functions or methods, and the input list can be of any length.
"""

def reverse_copy(input_list):
    """
    Creates a new list with the same elements as the input list, 
    but in reverse order, without modifying the original list.

    Args:
    input_list (list): The input list to be reversed.

    Returns:
    list: A new list with the elements in reverse order.
    """
    # Create a copy of the original list by slicing it
    copied_list = input_list[:]
    
    # Reverse the order of elements in the copied list
    # Using a two-pointer approach to swap elements from start and end
    left = 0
    right = len(copied_list) - 1
    while left < right:
        copied_list[left], copied_list[right] = copied_list[right], copied_list[left]
        left += 1
        right -= 1
    
    return copied_list