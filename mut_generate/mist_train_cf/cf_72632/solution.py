"""
QUESTION:
Write a function `pairs_sum_to_zero` that takes a list of integers as input. Return a list of all pairs of distinct elements in the list that sum to zero. The function must have a time complexity of O(n log n).
"""

def pairs_sum_to_zero(nums):
    pairs = []
    nums = sorted(nums)
    check_set = set()
    for i, num in enumerate(nums):
        if -num in check_set:
            pairs.append((-num, num))
        else:
            check_set.add(num)
    return pairs