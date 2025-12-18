"""
QUESTION:
Given an integer array `arr`, write a function `minSubarrayRemoval(arr)` to find the length of the shortest subarray that needs to be removed so that the remaining elements in `arr` are non-decreasing, the sum of the remaining elements is maximum, and the remaining elements form a palindrome. The length of `arr` is between 1 and 10^5 (inclusive), and each element in `arr` is between 0 and 10^9 (inclusive).
"""

def minSubarrayRemoval(arr):
    n = len(arr)

    # create prefix and suffix sum arrays
    prefix_sum = [0] * (n + 2)
    suffix_sum = [0] * (n + 2)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
        suffix_sum[n-i] = suffix_sum[n-i+1] + arr[n-i-1]

    # binary search
    def check(mid):
        for i in range(mid, n+1):
            total = prefix_sum[i] + suffix_sum[n+1-mid]
            if total >= suffix_sum[1]: return True
        return False

    left, right = 0, n
    while left < right:
        mid = (left + right + 1) >> 1
        if check(mid):
            right = mid - 1
        else:
            left = mid
    return n - left