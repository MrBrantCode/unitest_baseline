"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts a given list of numbers in-place from smallest to largest using a time complexity of O(n^2) and a space complexity of O(1), without using any built-in sorting functions or libraries.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr