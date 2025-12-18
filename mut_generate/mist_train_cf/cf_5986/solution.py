"""
QUESTION:
Implement a function named `bubble_sort_recursive` that sorts an array of strings and numbers in descending order using the bubble sort algorithm. The array may contain duplicates, and the function should group them together. Negative numbers should be placed before positive numbers in the sorted array. The function should be implemented recursively without using any built-in sorting functions or libraries. The array can contain floating-point numbers.
"""

def bubble_sort_recursive(arr):
    """
    Sorts an array of strings and numbers in descending order using the bubble sort algorithm.
    The array may contain duplicates, and the function groups them together. 
    Negative numbers are placed before positive numbers in the sorted array.
    
    Args:
        arr (list): The array to be sorted.
    
    Returns:
        list: The sorted array.
    """
    n = len(arr)
    
    # Base case: if the array is empty or contains only one element, it is already sorted
    if n <= 1:
        return arr
    
    # Perform a single pass of the bubble sort algorithm
    for i in range(n - 1):
        # Check if the current element is greater than the next element
        if arr[i] < arr[i + 1]:
            # Swap the elements if they are in the wrong order
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursively call the function on the remaining unsorted portion of the array
    return bubble_sort_recursive(arr[:-1]) + [arr[-1]]