"""
QUESTION:
Write a function called `find_max_number` that takes a list of integers as input and returns the maximum number in the list without using any built-in sorting or comparison functions. The function should iterate through the list to find the maximum number and return it.
"""

def find_max_number(num_list):
    max_num = num_list[0]
    for num in num_list[1:]:
        if num > max_num:
            max_num = num
    return max_num