"""
QUESTION:
Given a sorted list of positive integers and a target value, implement a function `twoSum` that returns the indices of two distinct numbers from the list that add up to the target value. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list.
"""

def twoSum(nums, target):
    # Initialize two pointers, left and right
    left, right = 0, len(nums) - 1
    
    # Loop until the pointers meet
    while left < right:
        # Calculate the sum of the current pair
        curr_sum = nums[left] + nums[right]
        
        # Check if the current pair adds up to the target
        if curr_sum == target:
            return [left, right]  # Return the indices of the pair
        
        # If the sum is less than the target, move the left pointer to the right
        elif curr_sum < target:
            left += 1
        
        # If the sum is greater than the target, move the right pointer to the left
        else:
            right -= 1
    
    # If no pair is found, return an empty list
    return []