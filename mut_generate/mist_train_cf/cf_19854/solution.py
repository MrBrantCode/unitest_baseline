"""
QUESTION:
Design a recursive function `bubbleSortRecursive` that takes a list of numbers `arr`, its size `n`, and a sorting order `order` as parameters, and sorts the list in-place in the specified order (either "ascending" or "descending") with a time complexity of O(n^2).
"""

def bubbleSortRecursive(arr, n, order):
    if n == 1:
        return
    
    for i in range(n-1):
        if (order == "ascending" and arr[i] > arr[i+1]) or (order == "descending" and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    bubbleSortRecursive(arr, n-1, order)