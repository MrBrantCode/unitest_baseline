"""
QUESTION:
Create a function `bubble_sort(arr)` that takes an array of integers as input and returns the array sorted in descending order. Additionally, ensure that all even numbers are placed before odd numbers in the sorted array. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            # Compare adjacent elements and swap if in the wrong order
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # Check if the current element is odd and the next element is even, swap them
            if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr