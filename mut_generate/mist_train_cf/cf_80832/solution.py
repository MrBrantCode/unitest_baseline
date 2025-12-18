"""
QUESTION:
Create a function `target_sum_subarray(nums, target)` that takes an array of integers `nums` and a target integer `target` as input and returns `True` if there exists a continuous subarray within `nums` whose elements sum up to `target`, and `False` otherwise.
"""

def target_sum_subarray(nums, target):
    left, total = 0, 0

    for right in range(len(nums)):
        total += nums[right]
        while total > target:
            total -= nums[left]
            left += 1
        if total == target:
            return True

    return False