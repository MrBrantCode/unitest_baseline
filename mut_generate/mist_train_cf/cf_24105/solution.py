"""
QUESTION:
Create a function `insert_element` that takes a sorted list of integers and an integer as input, and returns the list with the integer inserted in the correct position to maintain the sorted order. The list and the integer are not empty, and the list is initially sorted in ascending order.
"""

def insert_element(sorted_list, num):
    """
    Inserts a number into a sorted list while maintaining the sorted order.

    Args:
        sorted_list (list): A sorted list of integers.
        num (int): The number to be inserted into the list.

    Returns:
        list: The sorted list with the number inserted.
    """
    for i in range(len(sorted_list)):
        if num < sorted_list[i]:
            return sorted_list[:i] + [num] + sorted_list[i:]
    return sorted_list + [num]