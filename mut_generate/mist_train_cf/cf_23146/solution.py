"""
QUESTION:
Write a function named `bubble_sort` that sorts an array of integers in descending order using bubble sort with a single outer loop and a time complexity of O(n^2). The input array can contain both positive and negative integers and must have a length between 2 and 10,000 (inclusive). If the input array is already sorted in descending order, the function should return the array without performing any sorting operations.
"""

def bubble_sort(arr):
    n = len(arr)
    sorted = False
    
    for i in range(n):
        if sorted:
            return arr
        
        sorted = True
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
    
    return arr