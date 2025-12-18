"""
QUESTION:
Write a function `sum_even_numbers_excluding` that calculates the sum of even numbers in a given range (1 to n), excluding the number 500 and any even numbers divisible by 3. The function should take one argument `n` and return the calculated sum.
"""

def sum_even_numbers_excluding(n):
    return sum(i for i in range(2, n+1, 2) if i != 500 and i % 3 != 0)