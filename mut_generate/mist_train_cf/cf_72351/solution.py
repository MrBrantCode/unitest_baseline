"""
QUESTION:
Develop a function `largest_divisible_subset(nums)` that takes a list of numbers `nums` as input and returns the largest subset where each pair in the subset is divisible by each other. The function should handle an empty list and return an empty list in that case.
"""

def largest_divisible_subset(nums):
    if len(nums) == 0:
        return []

    nums.sort(reverse=True)
    subsets = [[num] for num in nums]
    max_subset_index = 0

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] % nums[i] == 0 and len(subsets[i]) < len(subsets[j]) + 1:
                subsets[i] = subsets[j] + [nums[i]]

        if len(subsets[i]) > len(subsets[max_subset_index]):
            max_subset_index = i

    return subsets[max_subset_index]