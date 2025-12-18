"""
QUESTION:
Write a function `compute_and_sort(nums)` that takes a list of integers `nums` as input, computes the cube of each number, calculates the total sum of the cubed numbers, and returns the total sum along with the sorted list of cubed numbers in ascending order.
"""

def compute_and_sort(nums):
    # Compute the cube of each number in the list.
    cube_nums = [num**3 for num in nums]
    # Compute the total sum of the cubed numbers.
    total_sum = sum(cube_nums)
    # Sort the cubed numbers in ascending order.
    sorted_nums = sorted(cube_nums)
    return total_sum, sorted_nums