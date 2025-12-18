"""
QUESTION:
Write a function named `sum_even_odd` that takes an integer `n` as input and returns the sum of all even numbers and the sum of all odd numbers between 1 and `n` (inclusive).
"""

def sum_even_odd(n):
    sum_even = 0
    sum_odd = 0

    for num in range(1, n+1):
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_even, sum_odd