"""
QUESTION:
Write a function `transform_lists` that takes three inputs: two lists `first_list` and `second_list`, and an integer `given_number`. The function should return a new list where each element is the product of the corresponding elements from `first_list` and `second_list` if both lists have the same length. If one list is shorter, the remaining elements from the longer list should be incremented by `given_number`.
"""

from itertools import zip_longest

def transform_lists(first_list, second_list, given_number):
    result = []
    for first, second in zip_longest(first_list, second_list, fillvalue=given_number):
        if second is given_number:
            result.append(first + given_number)
        elif first is given_number:
            result.append(second + given_number)
        else:
            result.append(first*second)
    return result