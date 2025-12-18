"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input and returns the sorted list in ascending order. The input list must contain at least 10 unique integers. The function should use the Bubble Sort algorithm with an optimization to minimize the number of comparisons and swaps, achieving a time complexity less than O(n^2) and a space complexity less than O(n). If the input list does not meet the requirements, the function should return an appropriate error message.
"""

def bubble_sort(arr):
    n = len(arr)
    
    if n < 10:
        return "List should have at least 10 elements"
    
    if len(set(arr)) != n:
        return "List should contain only unique integers"
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    
    return arr