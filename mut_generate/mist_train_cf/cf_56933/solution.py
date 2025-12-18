"""
QUESTION:
Create a function called `sort_list` that takes a list of numbers as input and returns the sorted list if it is already sorted in ascending order; otherwise, it returns `None`. The function should include a validation step to check if the input list is sorted in ascending order.
"""

def sort_list(nums):
    sorted_nums = sorted(nums)
    
    # Validation
    if sorted_nums != nums:
        return None
    else:
        return sorted_nums