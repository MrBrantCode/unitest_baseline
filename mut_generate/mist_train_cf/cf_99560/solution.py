"""
QUESTION:
Write a function `find_first_positive(nums)` that finds the first positive number in a list of integers. If no positive number is found, return the string "No positive number was found". The time complexity of the function should be less than O(n^2).
"""

def find_first_positive(nums):
    n = len(nums)
    present = [False] * (n+1)
    
    for i in range(n):
        if nums[i] > 0 and nums[i] <= n:
            present[nums[i]] = True
    
    for i in range(1, n+1):
        if not present[i]:
            return i
    
    return "No positive number was found"