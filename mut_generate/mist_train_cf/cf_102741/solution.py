"""
QUESTION:
Write a function named `sum_first_last` that takes a list of lists, where each inner list contains only positive integers, and returns a list containing the sum of the first and last elements of each inner list.
"""

def sum_first_last(my_list):
    result = []
    for inner_list in my_list:
        result.append(inner_list[0] + inner_list[-1])
    return result