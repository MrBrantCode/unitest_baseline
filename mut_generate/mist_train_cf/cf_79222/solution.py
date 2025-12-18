"""
QUESTION:
Write a function `third_smallest_and_largest` that takes a list of numbers as input and returns the third smallest and third largest unique elements. If the list does not have enough unique values (less than 3), return "Not enough unique elements". The function should not use any built-in sorting functions. The function should return a tuple of two numbers in the format (third smallest, third largest).
"""

import heapq

def third_smallest_and_largest(lst):
    unique_nums = list(set(lst))

    if len(unique_nums) < 3:
        return "Not enough unique elements"

    smallest_nums = heapq.nsmallest(3, unique_nums)
    largest_nums = heapq.nlargest(3, unique_nums)

    return smallest_nums[-1], largest_nums[-1]