"""
QUESTION:
Write a function `sum_to_zero` that takes a list of integers as input and returns a list of unique pairs of numbers that add up to zero. The function should accept both positive and negative numbers and should not include pairs that are duplicates or contain the same numbers in a different order.
"""

def sum_to_zero(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 0:
                pair = (nums[i], nums[j])
                if pair not in result and pair[::-1] not in result:
                    result.append(pair)
    return result