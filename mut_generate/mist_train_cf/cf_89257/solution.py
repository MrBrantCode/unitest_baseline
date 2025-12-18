"""
QUESTION:
Write a function named `find_pairs` that takes a list of integers `nums` and a target sum `target` as input and returns a list of all unique pairs of numbers in the list that add up to the target sum. The function should have a time complexity of O(n^2) or better and should not use any built-in functions or libraries. The input list may contain negative numbers and duplicates, but the output should only include unique pairs, and the order of the pairs does not matter.
"""

def find_pairs(nums, target):
    pairs = []
    nums.sort()  # Sort the list in ascending order

    # Use two pointers approach to find the pairs
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            right -= 1
            # Skip any duplicates
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs