"""
QUESTION:
Given a list of unique integers `nums`, return all possible subsets along with their sums in a list of tuples. The list should not contain duplicate subsets and can be in any order. The function should be named `subsets`. The constraints are 1 <= length of `nums` <= 10 and -10 <= `nums[i]` <= 10.
"""

def subsets(nums):
    result = [([], 0)]
    for num in nums:
        result += [(curr + [num], sum + num) for curr, sum in result]
    return result