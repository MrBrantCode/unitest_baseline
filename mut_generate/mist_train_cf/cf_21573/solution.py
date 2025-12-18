"""
QUESTION:
Implement a function `bubble_sort_descending` that takes an array of integers as input and sorts it in descending order in-place. The input array should contain at most 100,000 elements and each element should be a positive integer less than or equal to 10^6. The function should have a time complexity of O(n^2) and use a constant amount of extra space, i.e., O(1) space complexity.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr