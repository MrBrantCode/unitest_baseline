"""
QUESTION:
Write a function `minOperationsToHomogenize(nums)` to compute the minimal number of operations required to render all elements in the array identical. The function must take an array `nums` of `n` integers as input. In each operation, `n - 1` elements can be incremented by `1` or `1` element can be decremented by `1`. The length of `nums` ranges from 1 to 10^4, inclusive, and the elements in `nums` range from -10^9 to 10^9, inclusive.
"""

def minOperationsToHomogenize(nums):
    # Find the middle number (median)
    mid = sorted(nums)[len(nums) // 2]
    
    # Compute and return the total absolute difference with the median.
    return sum(abs(num - mid) for num in nums)