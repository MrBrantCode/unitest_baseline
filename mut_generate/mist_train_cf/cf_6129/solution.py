"""
QUESTION:
Write a function named find_two_numbers that takes in an array of positive integers and a target sum as input and returns the indices of two numbers in the array that add up to the target sum. If multiple pairs exist, return the pair with the smallest difference between the two numbers. If no such pair exists, return an empty array. The solution should have a time complexity of O(n), where n is the length of the array, and should not use any built-in methods, libraries, or extra space to store intermediate results.
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