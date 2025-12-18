"""
QUESTION:
Develop a function named `cumprod` that uses recursion to calculate the cumulative product of each element within the input array. The function should take an array `arr` and an optional parameter `n` initialized to 1. The function should return a list of cumulative products. The solution should have a time complexity of O(n) and require O(n) additional space.
"""

def cumprod(arr, n=1):
    if len(arr) == 0:
        return []
    return [arr[0] * n] + cumprod(arr[1:], arr[0] * n)