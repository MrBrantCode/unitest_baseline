"""
QUESTION:
Write a function `find_three_numbers` that takes a list of integers and a target number as input, and returns all unique combinations of three numbers in the list that sum up to the target number. The function should handle duplicate numbers in the list and return only unique combinations.
"""

def find_three_numbers(nums, target):
    nums.sort()

    combinations = set()

    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            num2 = nums[left]
            num3 = nums[right]

            if nums[i] + num2 + num3 == target:
                combinations.add((nums[i], num2, num3))
                left += 1
                right -= 1

            elif nums[i] + num2 + num3 < target:
                left += 1

            else:
                right -= 1

    return combinations