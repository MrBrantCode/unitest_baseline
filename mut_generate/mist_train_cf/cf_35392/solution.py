"""
QUESTION:
Given a list of k inner lists, where each inner list contains a set of integers, and a modulo value m, write a function `max_sum_of_squares_modulo_m` to calculate the maximum value of the sum of squares of integers modulo m, where you can select one integer from each inner list.

The function `max_sum_of_squares_modulo_m` takes three parameters: an integer k representing the number of inner lists, an integer m representing the modulo value, and a list of k inner lists. The function should return the maximum value of the sum of squares of integers modulo m.
"""

from typing import List

def max_sum_of_squares_modulo_m(k: int, m: int, list_of_list: List[List[int]]) -> int:
    max_sum = 0
    for i in range(k):
        max_sum += max([x**2 % m for x in list_of_list[i]])
    return max_sum % m