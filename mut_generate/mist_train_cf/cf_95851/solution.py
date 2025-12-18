"""
QUESTION:
Write a function `bubbleSortRecursive` that takes three parameters: `arr` (the list of numbers to be sorted), `n` (the size of the list), and `order` (specifying whether to sort in ascending or descending order). Implement a recursive Bubble Sort algorithm with a time complexity of O(n^2) to sort the list in-place according to the specified order.
"""

def bubbleSortRecursive(arr, n, order):
    if n == 1:
        return
    
    for i in range(n-1):
        if (order == "ascending" and arr[i] > arr[i+1]) or (order == "descending" and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    bubbleSortRecursive(arr, n-1, order)