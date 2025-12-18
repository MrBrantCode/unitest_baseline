"""
QUESTION:
Write a function named `quicksort_descending` that takes an array of integers as input and returns the array sorted in descending order. The function must be able to handle arrays of any length, including those with duplicates, and must have a time complexity of O(nlogn). Additionally, the function should be able to handle arrays with negative integers and floating-point numbers.
"""

def quicksort_descending(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort_descending(left) + [pivot] + quicksort_descending(right)