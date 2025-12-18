"""
QUESTION:
Write a function `find_duplicates` that takes a list of integers `nums` and returns a list of all duplicate numbers in `nums` in the order they appear. The function should have a time complexity of O(n^2) and a space complexity of O(1), without using any additional data structures or built-in functions.
"""

def find_duplicates(nums):
    duplicates = []
    n = len(nums)
    
    for i in range(n):
        if nums[i] is None:
            continue
        
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                duplicates.append(nums[i])
                nums[j] = None
    
    return duplicates