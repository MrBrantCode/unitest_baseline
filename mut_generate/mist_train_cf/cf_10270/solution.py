"""
QUESTION:
Create a function named bubble_sort_descending that sorts an array of numbers in descending order using a sorting algorithm such as bubble sort or selection sort, without using built-in sorting functions. The function should be able to handle arrays with duplicate numbers and negative numbers. The input and output should be lists of integers, and the function should return the sorted list in descending order.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr