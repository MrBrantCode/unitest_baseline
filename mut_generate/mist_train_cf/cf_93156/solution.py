"""
QUESTION:
Write a function named `remove_min_max` that takes a string of comma-separated numbers as input, removes the minimum and maximum values, and returns a string with the remaining numbers, also comma-separated. The input string will contain at least three numbers. The numbers in the output string should be in the same order as they appear in the input string. If there are multiple minimum or maximum values, remove all of them.
"""

def remove_min_max(nums):
    # Split the string into a list of numbers
    nums_list = [int(num) for num in nums.split(", ")]
    
    # Find the minimum and maximum values
    min_val = min(nums_list)
    max_val = max(nums_list)
    
    # Remove the minimum and maximum values from the list
    nums_list = [num for num in nums_list if num not in (min_val, max_val)]
    
    # Convert the list back to a string with comma-separated values
    result = ", ".join([str(num) for num in nums_list])
    
    return result