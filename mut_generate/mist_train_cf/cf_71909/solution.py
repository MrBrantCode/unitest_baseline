"""
QUESTION:
Define a function `sum_nineteen_seventeen_seq` that calculates the sum of numbers less than the input `m` that end with the digit 9 and are divisible by either 17 or 19. The function should take an integer `m` as input and return the computed sum.
"""

def sum_nineteen_seventeen_seq(m: int) -> int:
    result = 0

    for i in range(m):
        if str(i).endswith('9') and (i % 17 == 0 or i % 19 == 0):
            result += i

    return result