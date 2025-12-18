"""
QUESTION:
Implement a function named `bubble_sort` that sorts a given list of strings in descending order by length in-place without using any built-in sorting functions or methods. The function should not use any extra space for sorting other than the original list, and its time complexity should be less than O(n^2), where n is the length of the list.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if len(arr[j]) < len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr