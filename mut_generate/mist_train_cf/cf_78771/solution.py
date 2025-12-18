"""
QUESTION:
Write a function `find_median` that calculates the median of an array of integers. The function should accept a list of integers as input, sort the list, and return the median value. If the list has an odd number of elements, return the middle element. If the list has an even number of elements, return the average of the two middle elements. The function assumes the input list is not empty and contains at least one element.
"""

def find_median(input_arr):
    sorted_input_arr = sorted(input_arr)
    size = len(sorted_input_arr)

    if size % 2 == 1:
        return sorted_input_arr[size // 2]
    else:
        return (sorted_input_arr[size // 2 - 1] + sorted_input_arr[size // 2]) / 2