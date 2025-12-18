"""
QUESTION:
Write a function named `three_sum` that takes a sorted array of distinct positive integers and a target number as input. The function should return `True` if there exists a triplet in the array that sums up to the target number, and `False` otherwise. The solution should have a time complexity better than O(n^3).
"""

def three_sum(nums, target):
    nums.sort()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                return True
            elif total < target:
                left += 1
            else:
                right -= 1
    return False