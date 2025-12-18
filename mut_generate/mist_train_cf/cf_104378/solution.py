"""
QUESTION:
Write a function named `sum_odd_numbers` that calculates the sum of all odd integers between 1 and a given integer `n` (inclusive) using a while loop. The function should return the calculated sum.
"""

def sum_odd_numbers(n):
    sum_of_odd_numbers = 0
    num = 1

    while num <= n:
        if num % 2 != 0:
            sum_of_odd_numbers += num
        num += 1

    return sum_of_odd_numbers