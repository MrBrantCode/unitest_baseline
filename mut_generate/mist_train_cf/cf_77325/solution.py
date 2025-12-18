"""
QUESTION:
Create a function `is_armstrong_number(n)` that determines whether a given integer `n` is an Armstrong number. The function should consider that an Armstrong number of n digits is equal to the sum of the nth power of its digits. There are no restrictions on the input integer `n`.
"""

def is_armstrong_number(n):
    str_n = str(n)
    length = len(str_n)
    sum_of_cubes = sum(int(char)**length for char in str_n)
    return sum_of_cubes == n