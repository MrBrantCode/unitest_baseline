"""
QUESTION:
Write a function named `sort_array` that takes an array of 0s, 1s, and 2s as input and returns the sorted array with all 0s first, followed by all 1s, and then all 2s. The function should have a time complexity of O(n) and space complexity of O(1), where n is the number of elements in the input array.
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