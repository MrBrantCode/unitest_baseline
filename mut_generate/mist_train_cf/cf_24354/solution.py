"""
QUESTION:
Write a function `find_triplets` that takes an array of integers as input and returns all unique triplets in the array that sum to zero. The function should return triplets in any order, but the triplets themselves should be ordered in ascending order. Each number in the triplet can only be used once.
"""

def find_triplets(nums):
    """
    This function takes an array of integers as input and returns all unique triplets in the array that sum to zero.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of unique triplets, where each triplet is a list of three integers that sum to zero.
    """
    nums.sort()
    triplets = []
    
    for i in range(len(nums) - 2):
        # Skip the same result
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
                
    return triplets