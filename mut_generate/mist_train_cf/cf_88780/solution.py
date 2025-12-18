"""
QUESTION:
Write a function `find_duplicates` that takes in a list of integers `nums` and returns a list of all duplicate numbers in `nums`. The order of the numbers in the returned list should match the order in which they appear in the input list. The function should have a time complexity of O(n^2) and a space complexity of O(1), and it should not use any additional data structures except for the output list.
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