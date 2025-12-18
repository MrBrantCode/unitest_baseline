"""
QUESTION:
Create a function `sortDescending` that takes a list of integers as input and returns the list sorted in descending order. The function should not use any built-in sorting algorithms or methods that directly sort the list, but instead use a custom approach to sort the list.
"""

def sortDescending(num_list):
    """
    This function takes a list of integers as input, sorts it in descending order 
    using a custom approach and returns the sorted list.

    Args:
        num_list (list): A list of integers.

    Returns:
        list: The input list sorted in descending order.
    """
    # Iterate over the list to find the maximum element
    for i in range(len(num_list)):
        # Initialize max_index as the first element's index
        max_index = i
        # Iterate over the rest of the list to find the maximum element
        for j in range(i+1, len(num_list)):
            # If a greater element is found, update max_index
            if num_list[j] > num_list[max_index]:
                max_index = j
        # Swap the maximum element with the first element of the unsorted part of the list
        num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
    return num_list