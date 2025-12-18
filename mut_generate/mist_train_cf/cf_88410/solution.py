"""
QUESTION:
Write a function `find_kth_smallest_distinct_value(nums, k)` that takes a list of integers `nums` and an integer `k` as input. The function should return the kth smallest distinct value in the list. If k is larger than the number of distinct values in the list, return -1. The input list can contain duplicate values, and the time complexity of the solution should be O(n log n), where n is the size of the input list.
"""

def find_kth_smallest_distinct_value(nums, k):
    nums.sort()
    distinct_values = set(nums)
    distinct_values = sorted(list(distinct_values))
    if k > len(distinct_values):
        return -1
    return distinct_values[k - 1]