"""
QUESTION:
Define a function `five_mult_div_seq(n: int, start_range: int, end_range: int, m: int)` that generates and counts the number of times the digit 5 appears in both decreasing and increasing arithmetic sequences involving integers. The integers should be less than a provided 'n' and divisible by either 9, 14, or a third provided number 'm'. The function should validate against a given start and end number for the sequences. The integers should be within the range of 'start_range' and 'end_range' (inclusive).
"""

from functools import reduce

def five_mult_div_seq(n: int, start_range: int, end_range: int, m: int):
    numbers = [i for i in range(start_range, end_range+1) if (i < n) and (i % 9 == 0 or i % 14 == 0 or i % m == 0)]
    return reduce(lambda x, y: x + str(y).count("5"), numbers, 0)