"""
QUESTION:
Implement a function `twoSum(nums, target)` that takes a list of positive integers `nums` and a target value `target` as input and returns the indices of two distinct numbers from the list that add up to the target value. Assume that each input has exactly one solution, and you may not use the same element twice.
"""

def entance(nums, target):
    # Create an empty hash map
    num_map = {}
    
    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        
        # Check if the complement exists in the hash map
        if complement in num_map:
            # Return the indices of the two numbers
            return [num_map[complement], i]
        
        # Store the current number and its index in the hash map
        num_map[num] = i
    
    # If no solution is found, return an empty list
    return []