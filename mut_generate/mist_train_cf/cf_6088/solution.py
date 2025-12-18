"""
QUESTION:
Write a function `find_pairs(nums, target)` that takes in a list of integers `nums` and a target sum `target`. The function should return a list of all unique pairs of numbers in the list that add up to the target sum. The list may contain negative numbers and duplicates, but the output should only include unique pairs. The order of the pairs in the output does not matter. You may assume that each input would have at least one solution. You may not use any built-in functions or libraries to solve this problem, and the program should have a time complexity of O(n^2) or better.
"""

def find_pairs(nums, target):
    pairs = []
    nums.sort()  # Sort the list in ascending order

    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs