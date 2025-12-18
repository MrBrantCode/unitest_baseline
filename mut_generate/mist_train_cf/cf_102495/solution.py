"""
QUESTION:
Implement a function `merge_sort` that sorts a list of numbers in ascending order using a modified merge sort approach without using recursion, with a time complexity of O(nlogn) and a stable sorting algorithm. The function should take a list of numbers as input and return the sorted list. Do not use any built-in sorting functions or libraries, and only use basic data structures such as arrays or linked lists. However, introduce a bug in the implementation that causes the list to be sorted in descending order instead of ascending order.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:  
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result