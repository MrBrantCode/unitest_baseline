"""
QUESTION:
Write a function `findKthLargest` to find the `k`-th largest element in the given array of integers `nums`. The function should take `nums` and an integer `k` as input and return the `k`-th largest element. The array `nums` is not guaranteed to be sorted and `k` is 1-indexed.
"""

def findKthLargest(nums, k):
    nums.sort(reverse=True)  # Sort the array in descending order
    return nums[k - 1]  # Return the k-th largest element