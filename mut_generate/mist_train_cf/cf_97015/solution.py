"""
QUESTION:
Write a function named `twoSum` that takes in a list of integers `nums` and a target integer `target`, and returns a list of two integers representing the indices of the two numbers in `nums` that add up to `target`. The input list `nums` will contain at least 2 elements and at most 10^5 elements, and each element will be an integer in the range of -10^9 to 10^9, inclusive. The function should not use the same element twice and should return an empty list if no solution is found.
"""

def twoSum(nums, target):
    # Create a dictionary to store the complement of each number
    complement_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Add the current number and its index to the dictionary
        complement_dict[num] = i
    
    # If no solution is found, return an empty list
    return []