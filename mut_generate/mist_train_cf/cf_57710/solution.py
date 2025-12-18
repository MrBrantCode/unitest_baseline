"""
QUESTION:
Write a function named sum_nineteen_seventeen_seq(m) that calculates the cumulative sum of prime numbers less than m, where these numbers end with an odd single-digit number (1, 3, 5, 7, or 9) and are divisible by either 17 or 19.
"""

def sum_nineteen_seventeen_seq(m: int):
    total_sum = 0
    for i in range(2, m):
        if i == 17 or i == 19:
            total_sum += i
    return total_sum