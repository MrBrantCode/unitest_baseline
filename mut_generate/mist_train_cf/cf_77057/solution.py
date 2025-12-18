"""
QUESTION:
Write a Python function, `find_median`, to sort a collection of unique integers (including negative values) in ascending order without using any pre-built sorting functions and then identify and print the median value. The function should handle both odd and even lengths of input arrays.
"""

def find_median(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    if n % 2 == 0:  # if the length of the arr is even
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]
    return median