"""
QUESTION:
Write a function `count_even_numbers` that takes an integer `max` as input and returns the number of even positive integers less than `max`. The function should consider all even numbers, including perfect squares and cubes. The input `max` is the product of two distinct prime numbers.
"""

def count_even_numbers(max):
    count = 0
    for i in range(2, max, 2):
        count += 1
    return count