"""
QUESTION:
Implement a function named `insertion_sort_descending` to sort a given list of numbers in descending order. The function should use a well-optimized sorting algorithm with a time complexity of O(n^2) or better, without utilizing any built-in sorting functions or libraries. The function must handle edge cases, including empty lists and lists with duplicate numbers.
"""

def insertion_sort_descending(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr