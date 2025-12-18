"""
QUESTION:
Write a function `threeSum` that takes an array of integers `nums` and an integer `target` as input, and returns all unique triplets in the array that sum up to the target number. The function should return triplets in a list of lists format, and the triplets should be in non-decreasing order. The input array can contain duplicate elements, but the function should not return duplicate triplets. The time complexity should be O(n^2) or better, where n is the length of the input array.
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