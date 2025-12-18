"""
QUESTION:
Given a list of integers, write a function `find_missing_number(lst)` that finds the missing number that would make the sum of the input list a perfect square. The sum of the list with the missing number should be the square of an integer and the missing number should be the smallest possible integer to achieve this.
"""

import math

def find_missing_number(lst):
    sum_lst = sum(lst)
    n = len(lst) + 1
    perfect_square = int(math.sqrt(sum_lst + n*n))
    missing_number = perfect_square * perfect_square - sum_lst
    return missing_number