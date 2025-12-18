"""
QUESTION:
Implement a function `twoSum(nums, target)` that takes a list of integers `nums` and a target integer `target` as input, and returns a list of two indices of the numbers in `nums` that add up to `target`. The input list `nums` will always have at least two elements, and the target value will always have a valid pair of indices. The indices are 0-based and the function should return any one of the pairs that satisfy the condition if there are multiple.
"""

def entrance(nums, target):
    # Create a dictionary to store the complements of each number
    complements = {}
    
    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Check if the complement of the current number exists in the dictionary
        if target - num in complements:
            # If it does, return the indices of the two numbers
            return [complements[target - num], i]
        
        # If the complement does not exist, add the current number and its index to the dictionary
        complements[num] = i