"""
QUESTION:
Write a function named `find_three_numbers` that takes a list of integers `nums` and a target sum as input, and returns `True` if there exists a set of three unique numbers in the list that add up to the target sum, and `False` otherwise. The list may contain duplicate elements, but the solution should not include duplicate sets in its result.
"""

def find_three_numbers(nums, target):
    nums.sort()  # Sort the list in ascending order
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate elements to avoid duplicate sets
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                return True
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return False