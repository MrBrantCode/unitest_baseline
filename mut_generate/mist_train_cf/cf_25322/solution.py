"""
QUESTION:
Create a function `twoSum(N, arr)` that takes an integer `N` and a list of integers `arr` as input. The function should return a tuple of two integers from the list that add up to `N`. If no such pair exists, the function's behavior is unspecified. The function should return the first pair it finds that meets the condition, and it should not use the same number twice.
"""

def twoSum(N, arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == N:
                return (arr[i], arr[j])