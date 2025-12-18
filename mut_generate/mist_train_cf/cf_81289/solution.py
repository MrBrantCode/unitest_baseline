"""
QUESTION:
Write a function `maxSubArraySum(a)` that calculates the sum of all subarrays of a given array `a`. The function should return the maximum sum found amongst them. The function should consider all possible subarrays of the given array, including single-element subarrays.
"""

def maxSubArraySum(a):
    max_so_far = a[0]
    curr_max = a[0]
    for i in range(1, len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far