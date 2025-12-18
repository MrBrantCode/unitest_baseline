"""
QUESTION:
Implement the `bubble_sort_descending` function, which takes an array of numbers as input and sorts it in descending order using a modified bubble sort algorithm. The function should have a time complexity of O(n^2) and space complexity of O(1), and it should not use any additional data structures or built-in sorting functions. The input array may contain duplicate numbers and has a maximum length of 1000.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr