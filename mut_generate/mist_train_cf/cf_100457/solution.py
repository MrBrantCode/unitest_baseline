"""
QUESTION:
Write a function named `sum_to_zero` that takes a list of integers as input and returns a list of unique pairs of numbers that add up to zero. The function should work with lists containing both positive and negative numbers, and should exclude pairs that are duplicates when reversed.
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