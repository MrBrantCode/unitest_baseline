"""
QUESTION:
Write a function `can_partition_with_same_product(nums)` that takes an array of distinct positive integers as input and returns a boolean indicating whether it is possible to rearrange this array into two subsets with identical products. If `n > 18`, return "Can't be parsed".
"""

def can_partition_with_same_product(nums):
    if len(nums) > 18: return "Can't be parsed"

    total_product = 1
    for num in nums: 
        total_product *= num

    if total_product & 1: return "Not possible"

    nums.sort() 
    target_product = total_product // 2
    n = len(nums) 

    def can_partition(start, target_product):
        if target_product == 1: return True
        if target_product < nums[start]: return False
    
        for i in range(start, n):
            if nums[i] > target_product: break 
            if target_product % nums[i] == 0 and can_partition(i+1, target_product//nums[i]):
                return True

        return False

    return can_partition(0, target_product)