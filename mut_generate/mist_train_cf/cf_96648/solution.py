"""
QUESTION:
Implement a function named `bubble_sort_descending` that takes an array of positive integers as input and sorts them in descending order in-place. The input array should have at most 100,000 elements and each element should be less than or equal to 10^6. The implementation should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the input array.
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