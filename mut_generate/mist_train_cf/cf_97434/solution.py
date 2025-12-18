"""
QUESTION:
Write a function `subsetSum(nums, target)` that determines if a list of integers `nums` contains a subset that sums up to the target `target`. The function should also return all possible subsets that sum up to the target. The list `nums` may contain negative numbers and duplicate numbers. The function should have a time complexity of O(2^n) and a space complexity of O(n).
"""

def subsetSum(nums, target):
    def findSubsetSum(index, currentSum, subset, result):
        # Base Cases
        if currentSum == target:
            result.append(subset)
            return
        if index == len(nums):
            return
        
        # Recursive Cases
        # Include the current element
        findSubsetSum(index + 1, currentSum + nums[index], subset + [nums[index]], result)
        
        # Exclude the current element
        findSubsetSum(index + 1, currentSum, subset, result)

    result = []
    findSubsetSum(0, 0, [], result)
    if len(result) > 0:
        return True, result
    else:
        return False, []