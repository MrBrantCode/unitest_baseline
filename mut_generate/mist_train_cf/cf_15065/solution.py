"""
QUESTION:
Write a function `sort_array(arr)` that sorts an input array containing 0s, 1s, and 2s in ascending order with a time complexity of O(n) and space complexity of O(1). The function should return the sorted array.
"""

def sort_array(arr):
    # Initialize pointers
    left = 0  # pointer to the leftmost boundary of 1s
    mid = 0   # pointer to the current element being processed
    right = len(arr) - 1  # pointer to the rightmost boundary of 1s

    while mid <= right:
        if arr[mid] == 0:
            # Swap the element at mid with the element at left
            arr[mid], arr[left] = arr[left], arr[mid]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            # Swap the element at mid with the element at right
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

    return arr