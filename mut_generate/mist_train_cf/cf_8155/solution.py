"""
QUESTION:
Implement the function `quicksort` that takes an array of integers as input and returns the sorted array in ascending order. The function should have a time complexity of O(nlogn) or less and a space complexity of O(1), without using any built-in sorting functions or libraries.
"""

def quicksort(arr):
    """
    This function sorts the given array in ascending order using the Quicksort algorithm.
    
    Args:
    arr (list): A list of integers to be sorted.
    
    Returns:
    list: The sorted list of integers.
    """
    
    # Base case: If the array has one or zero elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Select the pivot element (in this case, the last element of the array).
    pivot = arr[-1]
    
    # Initialize pointers for the partition process.
    i = -1
    
    # Partition the array by rearranging the elements.
    for j in range(len(arr) - 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at the 'i + 1' index.
    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]
    
    # Recursively sort the sub-arrays on either side of the pivot.
    left = quicksort(arr[:i + 1])
    right = quicksort(arr[i + 2:])
    
    # Combine the sorted sub-arrays and the pivot element.
    return left + [arr[i + 1]] + right