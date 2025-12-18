"""
QUESTION:
Write a function `sum_nineteen_seventeen_seq(m)` that calculates the cumulative sum of all numbers less than `m` that end with the digit 9 and are divisible by either 17 or 19. The function should take an integer `m` as input and return the cumulative sum as an integer.
"""

def sum_nineteen_seventeen_seq(m: int) -> int:
    return sum(i for i in range(m) if i % 10 == 9 and (i % 17 == 0 or i % 19 == 0))