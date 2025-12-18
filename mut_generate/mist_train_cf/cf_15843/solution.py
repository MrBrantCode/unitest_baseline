"""
QUESTION:
Implement an iterative quick-sort function named `quicksort` that takes a list of elements as input and returns the sorted list in ascending order. The function should handle arrays with duplicate elements efficiently and have a time complexity of O(nlogn). It should not use any built-in sorting functions or libraries and must be implemented in an iterative manner instead of using recursion.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = arr[start]
        left = start + 1
        right = end

        while left <= right:
            if arr[left] <= pivot:
                left += 1
            elif arr[right] >= pivot:
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        arr[start], arr[right] = arr[right], arr[start]

        if right - 1 - start < end - (right + 1):
            stack.append((start, right - 1))
            stack.append((right + 1, end))
        else:
            stack.append((right + 1, end))
            stack.append((start, right - 1))

    return arr