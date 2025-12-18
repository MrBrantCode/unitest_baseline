"""
QUESTION:
Implement a function `find_sum_of_three(nums, target_sum)` that determines if any three numbers from the list `nums` sum up to the given `target_sum`. The function should run in O(n^2) time complexity and O(1) space complexity, where n is the length of the list. It cannot use any built-in sorting or searching functions.
"""

def find_sum_of_three(nums, target_sum):
    n = len(nums)
    for i in range(n - 2):
        num1 = nums[i]
        for j in range(i + 1, n - 1):
            num2 = nums[j]
            num3 = target_sum - (num1 + num2)
            for k in range(j + 1, n):
                if nums[k] == num3:
                    return True
    return False