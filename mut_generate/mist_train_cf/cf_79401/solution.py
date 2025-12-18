"""
QUESTION:
Implement a function `remove_duplicates_and_sort` that takes a list of integers as input and returns the list with duplicates removed and sorted in ascending order. The function should use the selection sort algorithm to sort the list.
"""

def remove_duplicates_and_sort(array):
    """
    This function takes a list of integers, removes duplicates, and sorts the list in ascending order.
    
    Args:
    array (list): A list of integers.
    
    Returns:
    list: A sorted list of integers with duplicates removed.
    """
    
    # Remove duplicates
    array = list(dict.fromkeys(array))
    
    # Sort array using selection sort
    for i in range(len(array)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted array      
        array[i], array[min_idx] = array[min_idx], array[i]

    return array