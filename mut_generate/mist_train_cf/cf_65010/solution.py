"""
QUESTION:
Create a function `sum_nineteen_seventeen_seq(m: int)` that calculates the sum of numbers less than `m` that end with digit 9 and are divisible by either 17 or 19. The input `m` is an integer, and the function should return the sum as an integer. The function should iterate through numbers from 0 to `m-1` to find the numbers that meet the conditions.
"""

def sum_nineteen_seventeen_seq(m: int):
    s = 0
    for n in range(m):
        if (n % 17 == 0 or n % 19 == 0) and (n % 10 == 9):
            s += n
    return s