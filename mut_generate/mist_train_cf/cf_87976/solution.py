"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in non-decreasing order. The function should have a time complexity of O(n^2), and should not use any built-in sorting functions or libraries. The input array can have a maximum length of 10^6 and the range of integers in the array is from -10^9 to 10^9. If there are any negative numbers in the array, the sorted array should be in non-increasing order.
"""

def bubble_sort(arr):
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