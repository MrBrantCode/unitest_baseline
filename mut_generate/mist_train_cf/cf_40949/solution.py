"""
QUESTION:
Implement a function `threeSum` that takes an array of integers `nums` and returns a list of lists containing all unique triplets that sum up to zero. The solution should not contain duplicate triplets, and the order of the elements in the output lists does not matter.
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to easily handle duplicates and for efficient traversal
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
            continue
        
        left, right = i + 1, len(nums) - 1  # Set pointers for the remaining array
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # Skip duplicate elements
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # Skip duplicate elements
                    right -= 1
                left += 1
                right -= 1
    
    return result