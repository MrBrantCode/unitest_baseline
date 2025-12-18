"""
QUESTION:
Create a function `find_divisible_numbers` that takes a list of integers as input. The function should return two separate lists: one containing all the even numbers that are divisible by 2, and the other containing all the odd numbers that are divisible by 3.
"""

from typing import List, Tuple

def find_divisible_numbers(input_list: List[int]) -> Tuple[List[int], List[int]]:
    div_by_2 = [num for num in input_list if num % 2 == 0]
    div_by_3 = [num for num in input_list if num % 2 != 0 and num % 3 == 0]
    return div_by_2, div_by_3