"""
QUESTION:
Write a function `remove_divisible_duplicates` that takes a list of integers and a specified value as input, and returns a new list with all numbers divisible by the specified value removed and no duplicates.
"""

def remove_divisible_duplicates(lst, value):
    modified_list = []
    for num in lst:
        if num % value != 0 and num not in modified_list:
            modified_list.append(num)
    return modified_list