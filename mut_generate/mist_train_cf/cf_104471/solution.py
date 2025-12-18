"""
QUESTION:
Write a function named `sort_list_descending` that takes a list of integers as input and returns a new list containing the same integers sorted in descending order with no duplicates. You cannot use any built-in sorting functions or methods.
"""

def sort_list_descending(nums):
    # Remove duplicates from the list
    unique_nums = list(set(nums))
    
    # Initialize an empty list to store the sorted numbers
    sorted_nums = []
    
    # Sort the numbers in descending order
    while unique_nums:
        max_num = unique_nums[0]
        for num in unique_nums:
            if num > max_num:
                max_num = num
        sorted_nums.append(max_num)
        unique_nums.remove(max_num)
    
    return sorted_nums