"""
QUESTION:
Implement a function `bubble_sort_descending` that sorts an array of numbers in descending order using a modified version of the bubble sort algorithm. The function should have a time complexity of O(n^2) and space complexity of O(1), where n is the length of the array. The array may contain duplicate numbers and has a maximum length of 1000. The function should not use any additional data structures or built-in sorting functions.
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