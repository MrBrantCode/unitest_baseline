"""
QUESTION:
Write a function `find_min_and_second_min(arr3D)` that takes a 3D array `arr3D` as input and returns the smallest and second smallest numbers in the array. The function should be able to handle duplicate values and find the second smallest unique number.
"""

def find_min_and_second_min(arr3D):
    # Flatten the 3D array to 1D array
    flat_list = [item for sublist in arr3D for subsublist in sublist for item in subsublist]

    # Sort the list in ascending order
    sorted_list = sorted(list(set(flat_list)))

    # The first and second elements in the sorted list are min and 2nd min respectively
    return sorted_list[0], sorted_list[1]