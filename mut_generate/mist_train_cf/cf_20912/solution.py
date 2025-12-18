"""
QUESTION:
Create a function named `binary_search` that implements a binary search algorithm to find the index of a given goal value in a sorted list. The function should take in three parameters: `arr` (the sorted list), `goal` (the value to search for), and `compare_fn` (a function that compares two elements in the list). The `compare_fn` function should take in two parameters: `a` and `b`, and should return a negative number if `a` is less than `b`, 0 if they are equal, or a positive number if `a` is greater than `b`. The function should return the index of `goal` if it is present in the list, or -1 if it is not found.
"""

def binary_search(arr, goal, compare_fn):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        comparison = compare_fn(arr[mid], goal)

        if comparison == 0:
            return mid
        elif comparison < 0:
            left = mid + 1
        else:
            right = mid - 1

    return -1