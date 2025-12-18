"""
QUESTION:
Implement the function `find_kth_largest` that finds the kth largest element in a list of integers. The function should take two parameters: `nums` (the list of integers) and `k` (the position of the desired element). 

The function should be able to handle input lists of any length, input lists with duplicate elements, negative integers, and floating-point numbers. The function should not use any built-in sorting functions or libraries. The time complexity of the function should be O(n) or better. If k is out of range, the function should return None.
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