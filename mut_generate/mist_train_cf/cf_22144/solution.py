"""
QUESTION:
Write a function twoSumWithMaxDifference(nums, target) that takes a list of distinct positive integers and a target integer as input, and returns a list of two indices of the numbers in the input list that sum up to the target value and have the maximum difference in their indices. The function should not use the same element twice, and each element in the list can only be used once.
"""

def twoSumWithMaxDifference(nums, target):
    numMap = {}
    result = []
    maxDifference = -1
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            difference = abs(i - numMap[complement])
            if difference > maxDifference:
                result = [numMap[complement], i]
                maxDifference = difference
        numMap[nums[i]] = i
    
    return result