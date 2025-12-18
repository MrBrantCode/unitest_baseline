"""
QUESTION:
Implement a function named `optimized_linear_search` that searches for an element `x` in an unsorted list `arr` by searching from both ends of the list. The function should return the index of the element if found, and -1 if not found. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list.
"""

def optimized_linear_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] == x:
            return left
        if arr[right] == x:
            return right

        left += 1
        right -= 1
    return -1