"""
QUESTION:
Develop a function `perfect_numbers(n)` that takes an integer `n` as input and returns a list of perfect numbers within the range from 0 to `n`. A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
"""

def perfect_numbers(n):
    perfect_numbers_list = []

    for i in range(1, n + 1):
        divisors_sum = 0
        for j in range(1, i):
            if i % j == 0:
                divisors_sum += j

        if divisors_sum == i:
            perfect_numbers_list.append(i)

    return perfect_numbers_list