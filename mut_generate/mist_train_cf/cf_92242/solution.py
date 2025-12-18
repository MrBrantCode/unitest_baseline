"""
QUESTION:
Write a function `calculate_median` that takes an array of numbers as input and returns the median number. The input array will always contain an odd number of elements. You cannot use any built-in functions or libraries to sort the array.
"""

def calculate_median(arr):
    length = len(arr)
    mid_index = length // 2
    median = None

    while median is None:
        less_count = 0
        for num in arr:
            if num < arr[mid_index]:
                less_count += 1

        if less_count == mid_index:
            median = arr[mid_index]
        elif less_count < mid_index:
            mid_index += 1
        else:
            mid_index -= 1

    return median