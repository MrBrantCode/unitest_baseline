"""
QUESTION:
Implement the quicksort function, which takes a list of integers as input and returns a sorted list of integers. The function should use the QuickSort algorithm, a divide-and-conquer approach that employs partitioning, recursive looping, and merging to sort the list. The function should not take any additional parameters.
"""

def quicksort(arr):
    """
    This function implements the QuickSort algorithm to sort a list of integers.
    
    :param arr: A list of integers
    :return: A sorted list of integers
    """
    
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Select the pivot element (in this case, the middle element)
    pivot = arr[len(arr) // 2]
    
    # Divide the array into three sub-arrays: elements less than the pivot, 
    # elements equal to the pivot, and elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the sub-arrays and combine the results
    return quicksort(left) + middle + quicksort(right)