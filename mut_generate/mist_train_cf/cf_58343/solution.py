"""
QUESTION:
Write a function `find_maximum_sum` that calculates the maximum sum of a subarray where no two elements are adjacent or share a common divisor greater than 1. The function should take a list of integers as input and return the maximum sum. 

The function should use auxiliary functions `gcd` to calculate the greatest common divisor of two numbers, and `pairwise_coprime` to check if all pairs of elements in a subarray do not share a divisor greater than 1. The function `no_adjacent_elements` checks if there are no adjacent elements between two indices.

Restrictions: The function should use dynamic programming to find the maximum sum. The input list will contain at least one element, and all elements will be positive integers.
"""

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers"""
    if a == 0:
        return b
    return gcd(b % a, a)


def pairwise_coprime(arr, start, end):
    """Check if all pairs of elements in subarray don't share a divisor > 1"""
    for i in range(start, end):
        for j in range(i + 1, end):
            if gcd(arr[i], arr[j]) > 1:
                return False
    return True


def no_adjacent_elements(prev_index, curr_index):
    """Check for no adjacent elements"""
    return abs(prev_index - curr_index) > 1


def find_maximum_sum(arr):
    """Calculate the maximum sum of a subarray with conditions"""
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = arr[i]
        for j in range(i - 1):
            if no_adjacent_elements(j, i) and pairwise_coprime(arr, j, i + 1):
                dp[i] = max(dp[i], dp[j] + arr[i])
        dp[i] = max(dp[i], dp[i-1])
    return dp[-1]