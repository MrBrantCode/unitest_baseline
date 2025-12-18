"""
QUESTION:
Write a function `find_second_highest` that takes a list of integers and floating point numbers as input and returns the second highest number in the list. The list can contain positive, negative, or zero numbers and may have duplicate values. The function should not use the built-in `sort` function or any external libraries. If the list does not have a second highest number, the function should return `None`.
"""

def find_second_highest(lst):
    max_num = second_max = float('-inf')  # Initialize both maxima to negative infinity
    for num in lst:
        if num > max_num:
            # New maximum found, second maximum becomes old maximum
            second_max, max_num = max_num, num
        elif max_num > num > second_max:
            # Number is between current maximum and second maximum
            second_max = num
    # If second_max is original value, list doesn't have a second maximum
    if second_max == float('-inf'):
        return None
    return second_max