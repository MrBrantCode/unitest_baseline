"""
QUESTION:
Write a function named "sort_and_sum" that takes a list of integers as input, converts it to a set, removes elements less than or equal to 1, sorts the remaining elements in descending order, and returns their sum. The input list may contain duplicate integers, negative integers, zero, and integers within the range -100 to 100, with a maximum of 1000 elements. 

The function should have the following signature: `def sort_and_sum(lst: List[int]) -> int:`
"""

from typing import List

def sort_and_sum(lst: List[int]) -> int:
    # Convert the list to a set
    unique_set = set(lst)

    # Remove any element less than or equal to 1
    unique_set = {x for x in unique_set if x > 1}

    # Sort the set in descending order
    sorted_set = sorted(unique_set, reverse=True)

    # Calculate the sum of the elements in the set
    sum_of_set = sum(sorted_set)

    return sum_of_set