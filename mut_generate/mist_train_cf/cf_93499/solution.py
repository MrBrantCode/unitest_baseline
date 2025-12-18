"""
QUESTION:
Write a function `threeSum(nums, target)` that takes an array of integers `nums` and a target integer `target` as input, and returns all unique triplets in `nums` that sum up to `target`. The function should assume that there may be duplicate triplets in the input array, but the output should not contain duplicates. The function should return triplets in non-descending order, with elements within each triplet also in non-descending order. The input array `nums` may contain duplicate elements, and the function should be efficient enough to handle large inputs.
"""

def threeSum(nums, target):
    nums.sort()
    result = []
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result