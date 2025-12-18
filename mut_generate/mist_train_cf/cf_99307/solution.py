"""
QUESTION:
Write a function named `quicksort_descending` to sort an array of integers in descending order. The array can be of any length, may contain duplicates, and may include negative integers and floating-point numbers. The function should have a time complexity of O(nlogn).
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