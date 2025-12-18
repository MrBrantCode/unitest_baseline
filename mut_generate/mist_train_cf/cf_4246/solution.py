"""
QUESTION:
Design a function named `recursive_sum` that takes an array of integers as input and returns the sum of all elements at even indices. The function should be a recursive algorithm and should be able to handle arrays containing both positive and negative integers. The input array can be of any length.
"""

def recursive_sum(arr):
    def helper(arr, index):
        if index >= len(arr):
            return 0
        elif index % 2 == 0:
            return arr[index] + helper(arr, index + 2)
        else:
            return helper(arr, index + 1)
    return helper(arr, 0)