"""
QUESTION:
Write a function `find_pair(nums, target_sum)` that takes a list of integers `nums` and a target sum `target_sum` as input, and returns a pair of unique integers in the list that add up to the target sum with the smallest absolute difference between the two integers. The function should have a time complexity of O(n), where n is the length of the list of integers. If there are multiple pairs with the same smallest absolute difference, any one of them can be returned.
"""

def find_pair(nums, target_sum):
    num_set = set()
    pair = None
    min_diff = float('inf')

    for num in nums:
        complement = target_sum - num
        if complement in num_set:
            diff = abs(complement - num)
            if diff < min_diff:
                pair = (complement, num)
                min_diff = diff
        num_set.add(num)

    return pair