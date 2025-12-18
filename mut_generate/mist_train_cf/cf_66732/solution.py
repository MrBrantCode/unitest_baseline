"""
QUESTION:
Write a function named `calc_max_disparity` that takes a two-dimensional array of integers as input and returns the maximum disparity between the smallest and largest integers across all possible sub-arrays. The function should not take any additional parameters other than the two-dimensional array.
"""

def calc_max_disparity(two_dim_array):
    # Flatten the two dimensional array
    flat_list = [item for sublist in two_dim_array for item in sublist]

    # Calculate maximum disparity
    max_disparity = max(flat_list) - min(flat_list)

    return max_disparity