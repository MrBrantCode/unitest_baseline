"""
QUESTION:
Implement the function `bubble_sort(array)` to sort an array in ascending order using the bubble sort algorithm. The function should optimize the process by returning immediately if the array is already sorted, thus avoiding unnecessary iterations.
"""

def bubble_sort(array):
    n = len(array)
    # Flag to check if any swaps occurred
    swapped = True
    
    # Iterate through the array
    for i in range(n):
        # If no swaps occurred in the previous iteration,
        # then the array is already sorted, so we return
        if not swapped:
            return
        
        # Reset the swapped flag for each iteration
        swapped = False
        
        # Iterate through the unsorted portion of the array
        for j in range(n-i-1):
            # Swap elements if they are in the wrong order
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True