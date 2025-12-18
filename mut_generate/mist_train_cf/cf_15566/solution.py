"""
QUESTION:
Create a function `remove_duplicates_and_sort` that takes a list of integers as input, removes duplicates while preserving the original order, and returns the resulting list in ascending order. The input list is guaranteed to be sorted in descending order.
"""

def remove_duplicates_and_sort(input_list):
    new_list = []
    for num in input_list:
        if num not in new_list:
            new_list.append(num)
    new_list.sort()
    return new_list