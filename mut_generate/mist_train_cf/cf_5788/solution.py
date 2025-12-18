"""
QUESTION:
Write a function `bubble_sort(arr)` that sorts a list of integers in ascending order using the Bubble Sort algorithm. The list must contain at least 10 unique integers. The function should return the sorted list or an error message if the input list does not meet the conditions. The algorithm should be optimized to minimize the number of comparisons and swaps, with a time complexity less than O(n^2) and a space complexity less than O(n).
"""

def entrance(arr):
    n = len(arr)
    
    # Check if the list has at least 10 elements
    if n < 10:
        return "List should have at least 10 elements"
    
    # Check if the list contains only unique integers
    if len(set(arr)) != n:
        return "List should contain only unique integers"
    
    # Optimized Bubble Sort algorithm
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    
    return arr