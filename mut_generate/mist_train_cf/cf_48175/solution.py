"""
QUESTION:
Create a function `max_sum_subsets(nums)` that takes a list of integers as input, generates all possible subsets of the input list, calculates the sum of each subset, and returns all subsets with the maximum sum. The input list may contain both positive and negative integers.
"""

def max_sum_subsets(nums):
    # The total number of subsets is 2^n. So generate numbers from 0..2^n
    max_sum = float('-inf')
    max_sum_subsets = []
    total_combinations = 2 ** len(nums)
    for count in range(total_combinations):
        subset = []
        subset_sum = 0
        for j in range(len(nums)):
            # check if jth bit in the counter is set. If set then print jth element from set.
            if (count & (1 << j)) > 0:
                subset.append(nums[j])
                subset_sum += nums[j]
        if subset_sum > max_sum:
            max_sum = subset_sum
            max_sum_subsets = [subset]
        elif subset_sum == max_sum:
            max_sum_subsets.append(subset)

    return max_sum_subsets