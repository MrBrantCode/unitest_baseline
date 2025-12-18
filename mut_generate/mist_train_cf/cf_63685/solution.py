"""
QUESTION:
Write a function named `sum_nineteen_seventeen_seq` that takes an integer `m` and returns the sum of numbers less than `m` that end with the digit 9 and are divisible by either 17 or 19.
"""

def sum_nineteen_seventeen_seq(m: int) -> int:
    return sum(i for i in range(9, m, 10) if i % 17 == 0 or i % 19 == 0)