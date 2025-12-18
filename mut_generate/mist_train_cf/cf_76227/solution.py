"""
QUESTION:
Implement the function `find_largest_number(input_list)` to find the largest number in a given list of integers. The function should take one argument, a list of integers, and return the largest integer in the list. The input list may contain duplicate values and is not guaranteed to be sorted.
"""

def find_largest_number(input_list):
    largest_num = input_list[0]
    for num in input_list:
        if num > largest_num:
            largest_num = num
    return largest_num