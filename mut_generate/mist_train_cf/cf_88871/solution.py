"""
QUESTION:
Implement the `custom_sort` function to sort an array of numbers in descending order using a custom sorting algorithm that is not built-in or commonly used in programming languages. The algorithm should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the input array. You are not allowed to use any external libraries or functions for sorting.
"""

def custom_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr