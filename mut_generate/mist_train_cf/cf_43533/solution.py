"""
QUESTION:
Write a function `sum_nineteen_seventeen_seq(m: int) -> int` that calculates the sum of all numbers below `m` that end with 9 and are divisible by either 17 or 19. The function should return the total sum as an integer.
"""

def sum_nineteen_seventeen_seq(m: int) -> int:
    total = 0
    for num in range(9, m, 10):  
        if num % 17 == 0 or num % 19 == 0:  
            total += num
    return total