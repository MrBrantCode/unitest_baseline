"""
QUESTION:
Given a list of integers in the range [1, n] with a length of n + 1, where n is a positive integer, write a function find_duplicate(nums) that finds the duplicate element in the list. The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any additional data structures such as sets or dictionaries.
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