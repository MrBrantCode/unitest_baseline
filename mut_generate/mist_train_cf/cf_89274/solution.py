"""
QUESTION:
Write a function named `find_two_numbers` that takes an array of positive integers `nums` and a target sum `target` as input. Return the indices of two numbers in the array that add up to the target sum with the smallest difference between the two numbers. If no such pair exists, return an empty array. The time complexity of the solution should be O(n), where n is the length of the array, and no extra space should be used.
"""

def find_two_numbers(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1

    return []