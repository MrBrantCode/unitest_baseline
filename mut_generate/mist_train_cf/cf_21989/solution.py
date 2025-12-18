"""
QUESTION:
Write a function named `find_four_elements` that takes a list of positive integers `nums` and a target value `target` as input, and returns all possible combinations of four elements in the list whose sum equals the target value. The function should have a time complexity of O(n^4) and a space complexity of O(n), where n is the length of the input list.
"""

def find_four_elements(nums, target):
    result = []
    n = len(nums)
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
    
    return result