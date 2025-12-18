"""
QUESTION:
Write a function `find_duplicate(nums)` that identifies a duplicate element in a list of integers `nums` where each integer is between 1 and the length of the list (inclusive) and appears at least once except for one integer that appears twice. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_duplicate(nums):
    n = len(nums)
    
    i = 0
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                return nums[i]
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    return None