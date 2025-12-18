"""
QUESTION:
Write a function called `find_small_nums` that takes a multidimensional array as input and returns the three smallest unique numbers in ascending order. If the array has less than three unique numbers, return all unique numbers.
"""

def find_small_nums(array):
    # Flatten the array
    flat_list = [num for sublist in array for num in sublist]
    # Sort the list
    flat_list.sort()
    # Remove duplicates
    unique_nums = list(set(flat_list))
    # Sort the unique numbers
    unique_nums.sort()
    # Return the smallest three numbers, or all numbers if there are less than 3.
    return unique_nums[:3] if len(unique_nums) > 3 else unique_nums