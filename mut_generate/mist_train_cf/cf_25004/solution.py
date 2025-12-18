"""
QUESTION:
Write a function `find_triplets` that takes a sorted array of integers as input and returns the number of unique triplets in the array that sum up to zero. The function should ignore duplicate triplets.
"""

def find_triplets(nums):
    """
    This function takes a sorted array of integers as input and returns the number of unique triplets in the array that sum up to zero.
    
    Args:
    nums (list): A sorted list of integers.
    
    Returns:
    int: The number of unique triplets that sum up to zero.
    """
    res = set()
    nums.sort()
    for i in range(len(nums) - 2):
        # Skip the same result
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.add((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return len(res)