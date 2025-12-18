"""
QUESTION:
Create a function named `find_max_length` that takes a list of numbers as input and returns the maximum length of a strictly increasing subarray. The list can contain integers and/or floating-point numbers, and may have duplicate elements. The function should round floating-point numbers to the nearest whole number before performing calculations. If the input list is empty, return -1; if the list contains only one element, return 0.
"""

def find_max_length(nums):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        # Round the numbers to the nearest whole number
        rounded_num = round(nums[i])

        if rounded_num > round(nums[i - 1]):
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1

    if current_length > max_length:
        max_length = current_length

    return max_length