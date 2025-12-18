"""
QUESTION:
Implement a function named `reverse_list` that takes a list `arr` and reverses its order in-place using a recursive algorithm with O(1) space complexity. The function should be able to handle lists with duplicate elements.
"""

def reverse_list(arr):
    def reverse(start, end):
        if start >= end:
            return

        # Swap the first and last elements
        arr[start], arr[end] = arr[end], arr[start]

        # Reverse the remaining sublist
        reverse(start+1, end-1)

    reverse(0, len(arr)-1)