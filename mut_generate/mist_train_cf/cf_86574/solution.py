"""
QUESTION:
Write a function `sum_of_odd_numbers(n)` that calculates the sum of the first n odd numbers, excluding any number divisible by both 3 and 5. The function should return the sum modulo 10^9+7.
"""

def sum_of_odd_numbers(n):
    total_sum = 0
    count_divisible = 0

    for i in range(1, 2*n + 1, 2):
        if i % 3 == 0 and i % 5 == 0:
            count_divisible += 1
        else:
            total_sum += i

    return total_sum % (10**9 + 7)