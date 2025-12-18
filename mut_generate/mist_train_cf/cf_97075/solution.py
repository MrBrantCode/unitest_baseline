"""
QUESTION:
Implement a function `twoSum(nums, target)` that takes a list of distinct positive integers `nums` and a target integer `target` as input, and returns a list of two distinct indices `[i, j]` such that `nums[i] + nums[j] = target`. Assume that each input has exactly one solution, and the function must use an efficient data structure to achieve a solution in a single pass through the input list.
"""

def twoSum(nums, target):
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