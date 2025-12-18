"""
QUESTION:
Write a function called `binary_search` that takes a list of integers `nums` and an integer `target` as input, and returns whether the target element exists in the list. The function should implement a binary search approach on the sorted list. The list should be sorted in ascending order before performing the binary search, and the search should be performed without using any built-in search functions.
"""

def binary_search(nums, target):
    # Sort the list in ascending order
    nums.sort()
    
    # Initialize the search range
    left = 0
    right = len(nums) - 1
    
    found = False
    
    while left <= right:
        # Find the middle element
        mid = (left + right) // 2
        
        # Check if the middle element is equal to the target
        if nums[mid] == target:
            found = True
            break
        # Check if the target is less than the middle element
        elif target < nums[mid]:
            right = mid - 1
        # Check if the target is greater than the middle element
        else:
            left = mid + 1
    
    return found