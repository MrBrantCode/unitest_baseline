"""
QUESTION:
Implement a function `sort_list` that sorts a given list in increasing order without using any built-in sorting functions or methods, additional data structures, or helper functions. The list may contain duplicate elements and the solution should have a time complexity of O(n^2). The function should only use nested loops to implement the sorting algorithm.
"""

def sort_list(input_list):
    """
    Sorts a given list in increasing order without using any built-in sorting functions or methods.
    
    Args:
    input_list (list): The list to be sorted.
    
    Returns:
    list: The sorted list in increasing order.
    """
    
    n = len(input_list)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                
    return input_list