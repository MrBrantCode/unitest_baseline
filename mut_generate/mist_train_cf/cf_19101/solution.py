"""
QUESTION:
Write a function `remove_divisible_duplicates` that takes a list of integers `lst` and a specified integer `value` as input, and returns a list with all numbers divisible by `value` and duplicates removed. The order of elements in the original list should be preserved in the output.
"""

def remove_divisible_duplicates(lst, value):
    modified_list = []
    for num in lst:
        if num % value != 0 and num not in modified_list:
            modified_list.append(num)
    return modified_list