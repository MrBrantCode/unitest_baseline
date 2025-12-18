"""
QUESTION:
Write a function named `sort_integer_list` that takes a list of integers as input and returns the sorted list. The function should handle erroneous inputs by returning an error message if the input is not a list or if the list contains non-integer values.
"""

def sort_integer_list(nums):
    if type(nums) != list: 
        return "Error: Input should be a list."
    else: 
        try: 
            nums = [int(i) for i in nums] 
            nums.sort() 
            return nums
        except ValueError: 
            return "Error: List should only contain integers."