"""
QUESTION:
Create a function named `remove_duplicates_and_sort_descending` that takes a list of positive integers as input, raises each integer to the power of 2, removes duplicates, and returns the resulting list sorted in descending order.
"""

def remove_duplicates_and_sort_descending(nums):
    # Remove duplicates
    unique_nums = list(set(nums))
    
    # Raise each integer to the power of 2
    squared_nums = [num ** 2 for num in unique_nums]
    
    # Sort the list in descending order
    sorted_nums = sorted(squared_nums, reverse=True)
    
    return sorted_nums