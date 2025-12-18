"""
QUESTION:
Implement a recursive function `bubbleSort(arr, n)` that sorts the elements of the array `arr` in ascending order in-place using the Bubble Sort algorithm. The function should not use any additional space and have a time complexity of O(n^2), where n is the size of the array. The input to the function will be the array `arr` and its size `n`, and the function should sort the array in-place without returning any value.
"""

def bubbleSort(arr, n):
    # Base case: If array is empty or has only one element, it is already sorted
    if n <= 1:
        return
    
    # One pass of Bubble Sort. After this pass, the largest element will be at the end of the array.
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursively call bubbleSort on the remaining (n-1) elements
    bubbleSort(arr, n - 1)