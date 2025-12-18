"""
QUESTION:
Implement a recursive binary search function called `binary_search` that takes a sorted list of integers `arr` and a target integer `target` as input, and returns the index of the target in the list and the number of comparisons made during the search process. If the target is not found, return -1 as the index. The function should not use any loops, only recursive calls.
"""

def binary_search(arr, target):
    def binary_search_helper(arr, target, left, right, comparisons):
        if left > right:
            return -1, comparisons

        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            return binary_search_helper(arr, target, mid + 1, right, comparisons)
        else:
            return binary_search_helper(arr, target, left, mid - 1, comparisons)

    return binary_search_helper(arr, target, 0, len(arr) - 1, 0)