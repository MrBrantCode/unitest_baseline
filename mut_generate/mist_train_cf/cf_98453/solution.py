"""
QUESTION:
Create a function called `find_first_positive(nums)` that takes a list of integers `nums` as input and returns the first positive integer if it exists. If no positive integer exists, return the string "No positive number was found". The function should have a time complexity of less than O(n^2).
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