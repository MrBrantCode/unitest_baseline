"""
QUESTION:
Write a function `bubble_sort(arr)` that sorts the given list of integers from highest to lowest using the bubble sort algorithm without using any built-in sorting functions. The length of the list will be between 1 and 10^4, and the range of the numbers in the list will be between -10^9 and 10^9. The time complexity of the sorting algorithm should be O(n^2) and the space complexity should be O(1).
"""

def entance(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr