"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts an array of integers in non-decreasing order using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. The input array can be empty and may contain duplicate elements, with a maximum length of 10^6 and a range of integers from -10^9 to 10^9. If the input array contains any negative numbers, the function should return the sorted array in non-increasing order.
"""

def entrance(arr):
    n = len(arr)
    
    # Iterate through the entire array
    for i in range(n):
        # Flag to check if any swaps are made in this iteration
        swapped = False
        
        # Iterate from 0 to n-i-1, as the largest element will be moved to the end in each iteration
        for j in range(0, n-i-1):
            
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                # Set swapped flag to True
                swapped = True
                
        # If no swaps are made in an iteration, the array is already sorted
        if not swapped:
            break
    
    # If there are any negative numbers, reverse the array to ensure non-increasing order
    if any(num < 0 for num in arr):
        arr.reverse()
    
    return arr