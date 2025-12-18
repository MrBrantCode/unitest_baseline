"""
QUESTION:
Implement a method `subsets` in a class that takes a list of integers `nums` as input and returns all possible subsets of the input list. The method should generate all subsets, including the empty set and the set containing all elements of the input list.
"""

def subsets(nums):
    result = []
    backtrack(nums, 0, [], result)
    return result

def backtrack(nums, start, subset, result):
    result.append(subset[:])
    for i in range(start, len(nums)):
        subset.append(nums[i])
        backtrack(nums, i + 1, subset, result)
        subset.pop()