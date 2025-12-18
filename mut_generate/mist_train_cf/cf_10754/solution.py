"""
QUESTION:
Create a function `remove_duplicates` that takes a list of integers as input. Remove duplicate items from the list without using any built-in functions or additional data structures. The function should return or print the list of non-duplicate items.
"""

def remove_duplicates(nums):
    if len(nums) <= 1:
        return nums

    nums.sort()
    result = []
    last_num = nums[0]

    for num in nums[1:]:
        if num == last_num:
            continue
        else:
            result.append(last_num)
            last_num = num

    result.append(last_num)
    return result