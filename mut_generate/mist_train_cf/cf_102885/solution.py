"""
QUESTION:
Create a function `find_indices(nums, target)` that takes a list of unique numbers `nums` and a target number `target` as input. The function should return the indices of the two elements in `nums` that sum to `target` with the smallest difference between the two elements. If multiple pairs have the same smallest difference, any of them can be returned. If no such pair exists, return an empty list.
"""

def find_indices(nums, target):
    nums = [(i, num) for i, num in enumerate(nums)]
    nums.sort(key=lambda x: x[1])
    left, right = 0, len(nums) - 1
    smallest_difference = float('inf')
    result = []

    while left < right:
        total = nums[left][1] + nums[right][1]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            if abs(nums[left][1] - nums[right][1]) < smallest_difference:
                smallest_difference = abs(nums[left][1] - nums[right][1])
                result = [nums[left][0], nums[right][0]]
            left += 1
            right -= 1

    return result