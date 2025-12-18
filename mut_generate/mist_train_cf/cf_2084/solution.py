"""
QUESTION:
Write a function `remove_elements(nums, target)` that takes in a list of integers `nums` and a target integer `target`, removes all occurrences of the target integer from the list while preserving the order of the remaining elements, and returns the modified list. The function should use constant space complexity and achieve a time complexity of O(n), where n is the length of the input list.
"""

def remove_elements(nums, target):
    left = 0  
    for right in range(len(nums)):  
        if nums[right] != target:  
            nums[left] = nums[right]
            left += 1  
    return nums[:left]