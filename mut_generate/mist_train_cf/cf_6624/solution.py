"""
QUESTION:
Implement a function `find_kth_largest(nums, k)` that finds the kth largest element in a list of integers. The function should handle input lists of any length, duplicate elements, negative integers, and floating-point numbers. The function should not use any built-in sorting functions or libraries and should have a time complexity of O(n) or better. The input parameters are a list of integers `nums` and an integer `k` representing the position of the desired element. If `k` is out of range, the function should return `None`.
"""

def find_kth_largest(nums, k):
    if k < 1 or k > len(nums):
        return None
    pivot = nums[0]
    smaller = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    larger = [x for x in nums if x > pivot]
    if len(larger) >= k:
        return find_kth_largest(larger, k)
    elif len(larger) + len(equal) >= k:
        return pivot
    else:
        return find_kth_largest(smaller, k - len(larger) - len(equal))