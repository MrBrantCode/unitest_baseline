"""
QUESTION:
Write a function `movesToMakeZigzag(nums)` that takes an array of integers `nums` as input and returns the least number of moves required to convert the array into a zigzag array. A zigzag array is an array where every element at an even index surpasses its neighboring elements or every element at an odd index surpasses its neighboring elements. A move is defined as reducing any element by 1. The constraints are `1 <= nums.length <= 1000` and `1 <= nums[i] <= 1000`.
"""

def movesToMakeZigzag(nums):
    nums = [float('inf')] + nums + [float('inf')]
    even, odd = [0, 0]
   
    for i in range(1, len(nums) - 1):
        left,right = nums[i - 1], nums[i + 1]
        
        if i % 2 == 0:
            even += max(0, nums[i] - min(left, right) + 1)
        else:
            odd += max(0, nums[i] - min(left, right) + 1)

    return min(even, odd)