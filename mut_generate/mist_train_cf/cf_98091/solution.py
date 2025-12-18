"""
QUESTION:
Write a function `sum_even_numbers(n)` that calculates the sum of even numbers in the sequence of the first `n` positive integers using a loop structure. The function should take an integer `n` as input and return the sum of even numbers. The input `n` is a positive integer.
"""

def sum_even_numbers(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum