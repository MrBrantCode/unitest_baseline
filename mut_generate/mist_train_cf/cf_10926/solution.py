"""
QUESTION:
Develop a function named `round_array` that takes an array of real numbers as input and returns a new array with each number rounded to its nearest integer. If the decimal part of a number is greater than 0.5, round up; otherwise, round down. The function should achieve this in linear time complexity, O(n), where n is the length of the input array.
"""

def round_array(arr):
    rounded_array = []
    for num in arr:
        rounded_num = int(num)
        if num - rounded_num > 0.5:
            rounded_num += 1
        rounded_array.append(rounded_num)
    return rounded_array