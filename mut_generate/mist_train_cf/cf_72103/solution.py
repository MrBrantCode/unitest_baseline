"""
QUESTION:
Implement a function named `optimize_arrangement` that takes an array of unique integers as input and returns a dictionary. The dictionary should include the smallest index of an element which is not lesser than or equal to the preceding element ('index'), the index of the following greater element that can be swapped to ordering the sequence ('swap_with'), and the total count of needed swaps ('total_swaps'). If the input array is already sorted in ascending order, return {'index': -1, 'swap_with': -1, 'total_swaps': 0}. The function should modify the input array to swap the elements at the 'index' and 'swap_with' positions if a swap is necessary.
"""

def optimize_arrangement(lst):
    """
    This function takes an array of unique integers as input and returns a dictionary.
    The dictionary includes the smallest index of an element which is not lesser than or equal to the preceding element ('index'), 
    the index of the following greater element that can be swapped to ordering the sequence ('swap_with'), 
    and the total count of needed swaps ('total_swaps'). 
    If the input array is already sorted in ascending order, return {'index': -1, 'swap_with': -1, 'total_swaps': 0}.
    The function modifies the input array to swap the elements at the 'index' and 'swap_with' positions if a swap is necessary.
    
    Args:
        lst (list): A list of unique integers.
    
    Returns:
        dict: A dictionary containing 'index', 'swap_with', and 'total_swaps' for the input list.
    """

    index = -1
    swap_with = -1
    total_swaps = 0
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            index = i
            swap_with = i + 1
            total_swaps += 1
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            return {'index': index, 'swap_with': swap_with, 'total_swaps': total_swaps}
    return {'index': -1, 'swap_with': -1, 'total_swaps': 0}