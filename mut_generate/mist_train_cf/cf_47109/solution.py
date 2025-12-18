"""
QUESTION:
Write a function `closest_nums(nums)` that takes a list of numbers `nums` with at least two elements and returns the pair of numbers with the smallest difference in ascending order. The function should have a time complexity of O(n) and handle edge cases such as lists with less than three elements.
"""

def findClosestNums(nums):
    min_num = second_min_num = float('inf')
    min_diff = float('inf')
    closest_pair = ()

    for num in nums:
        if num <= min_num:
            second_min_num = min_num
            min_num = num
        elif num < second_min_num:
            second_min_num = num

    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] < min_diff:
            min_diff = nums[i + 1] - nums[i]
            closest_pair = (nums[i], nums[i + 1])

    if second_min_num - min_num < min_diff:
        return (min_num, second_min_num)
    else:
        return closest_pair