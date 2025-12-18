"""
QUESTION:
Write a function `find_kth_smallest_distinct_value` that takes a list of integers `nums` and an integer `k` as input. Return the kth smallest distinct value in the list. If k is larger than the number of distinct values in the list, return -1. The function should have a time complexity of O(n log n).
"""

def find_kth_smallest_distinct_value(nums, k):
    nums.sort()
    distinct_values = set()
    for num in nums:
        distinct_values.add(num)
    distinct_values = sorted(list(distinct_values))
    if k > len(distinct_values):
        return -1
    return distinct_values[k - 1]