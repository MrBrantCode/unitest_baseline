"""
QUESTION:
Write a function named sum_even_numbers to calculate the sum of even numbers from 1 to a given positive integer n using a loop structure in Python. The function should take one argument, n, and return the sum of even numbers.
"""

def sum_even_numbers(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum