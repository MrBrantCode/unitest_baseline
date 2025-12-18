"""
QUESTION:
Write a function `process_integers` that takes a list of integers as input, removes duplicates, sorts the list in ascending order, calculates the sum of the integers, and calculates the product of the integers. The function should return a tuple containing the sorted list with duplicates removed, the sum of the integers, and the product of the integers. The input list can contain duplicate integers and the product of the integers should be calculated using the unique integers.
"""

from typing import List, Tuple

def process_integers(input_list: List[int]) -> Tuple[List[int], int, int]:
    unique_sorted_list = sorted(list(set(input_list)))
    sum_of_integers = sum(unique_sorted_list)
    product_of_integers = 1
    for num in unique_sorted_list:
        product_of_integers *= num
    return unique_sorted_list, sum_of_integers, product_of_integers