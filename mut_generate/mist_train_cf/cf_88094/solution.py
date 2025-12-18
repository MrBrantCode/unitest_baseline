"""
QUESTION:
Implement a recursive Bubble Sort function named `bubbleSort` that sorts an array of integers in ascending order in-place without using any additional space. The function should take two parameters: `arr` (the array to be sorted) and `n` (the size of the array). The time complexity of your solution should be O(n^2).
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