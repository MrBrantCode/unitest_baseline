"""
QUESTION:
Write a function `findSubsets(arr, n, sumVal, dp)` that determines whether it's possible to divide an array `arr` of length `n` into two distinct subsets with identical products. The function should use dynamic programming and return `True` if such subsets exist, `False` otherwise. The product of all numbers in the array must be a perfect square or a perfect cube to ensure the two subsets have the same product. Assume that the input array only contains positive integers and the product of the entire array can be represented as a reasonably sized integer.
"""

def findSubsets(arr, n, sumVal, dp):
    if sumVal == 0:
        return True

    if n == 0 or sumVal < 0:
        return False

    key = (n, sumVal)

    if key not in dp:
        include = findSubsets(arr, n-1, sumVal/arr[n-1], dp)
        exclude = findSubsets(arr, n-1, sumVal, dp)

        dp[key] = include or exclude

    return dp[key]