"""
QUESTION:
Implement a function `bubbleSort(arr)` that sorts a list of elements in ascending order using the bubble sort algorithm. The function should take a list of elements as input, and return the sorted list. The function should have a time complexity of O(n^2) and space complexity of O(1).
"""

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        already_sorted = True
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        
        if already_sorted:
            break

    return arr