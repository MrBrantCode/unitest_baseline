"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input and returns the sorted list in ascending order using the bubble sort algorithm. The function should use nested loops to compare adjacent elements and swap them if they are in the wrong order. A flag variable should be used to optimize the sorting process and stop early if the list is already sorted. The function should not use built-in sorting functions or pre-existing sorting algorithms.
"""

def bubble_sort(arr):
    """
    Sorts a list using the bubble sort algorithm.
    
    Args:
    arr (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)  # Number of elements in the list
    sorted_arr = list(arr)  # Create a copy of the original list
    
    # Iterate through the list until it is sorted
    for i in range(n):
        swapped = False  # Flag variable to optimize the sorting process
        
        # Iterate through the list from index 0 to n-i-1
        # (The last i elements are already in place)
        for j in range(0, n-i-1):
            
            # Compare adjacent elements and swap them if they are in the wrong order
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
                swapped = True  # Set the flag variable to True
                
        # If no swaps were made in a pass, the list is already sorted
        if not swapped:
            break
    
    return sorted_arr