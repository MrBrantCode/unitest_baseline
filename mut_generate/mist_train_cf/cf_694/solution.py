"""
QUESTION:
Implement a function named `sort_list` that takes a list of integers as input and sorts it in increasing order. The function should not use any built-in sorting functions or methods, additional data structures, or helper functions. The solution should have a time complexity of O(n^2) and use nested loops.
"""

def sort_list(my_list):
    """
    Sorts the given list of integers in increasing order using Bubble Sort algorithm.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: The sorted list in increasing order.
    """

    n = len(my_list)

    for i in range(n-1):
        for j in range(n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                
    return my_list