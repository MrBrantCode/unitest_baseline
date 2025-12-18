"""
QUESTION:
Write a function `getSum` that takes a list of integers as input and returns the sum of all integers in the list. The function must use a recursive approach and should not modify the input list. If necessary, a helper function can be used.
"""

def getSum(arr):
    def helper(arr, index):
        if index == len(arr):
            return 0
        return arr[index] + helper(arr, index + 1)

    return helper(arr, 0)