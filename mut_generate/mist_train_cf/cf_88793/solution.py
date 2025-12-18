"""
QUESTION:
Write a function named `threeSum` that takes two parameters: a list of numbers `nums` and a target sum `target`. The function should determine if any three numbers from the list sum up to the given sum. The function must run in O(n^2) time complexity and O(1) space complexity, where n is the length of the list, and cannot use any built-in sorting or searching functions.
"""

def threeSum(nums, target):
    n = len(nums)
    for i in range(n-2):
        num1 = nums[i]
        for j in range(i+1, n-1):
            num2 = nums[j]
            num3 = target - num1 - num2
            for k in range(j+1, n):
                if nums[k] == num3:
                    return True
    return False