"""
QUESTION:
Write a function named `count_unique_pairs` that takes a list of numbers `nums` and a target sum `target_sum` as parameters. The function should return the number of unique pairs in the list whose combined sum equals the target sum, without counting pairs with swapped elements as separate pairs. The function should handle edge cases such as an empty list or a list with only one element, and should be efficient in terms of time and space complexity.
"""

def count_unique_pairs(nums, target_sum):
    if len(nums) < 2: 
        return 0

    nums = sorted(nums)
    pairs = set()

    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target_sum:
            pairs.add((nums[left], nums[right]))
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return len(pairs)