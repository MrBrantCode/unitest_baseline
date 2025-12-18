"""
QUESTION:
Create a function `compute_sum_of_multiples(num)` that takes an integer `num` as input and returns the sum of all natural numbers that are multiples of 3 or 5 and are less than `num`.
"""

def compute_sum_of_multiples(num):
    return sum(i for i in range(1, num) if i % 3 == 0 or i % 5 == 0)