"""
QUESTION:
Write a function named `sum_odd_multiples` that calculates the sum of all odd numbers in a given array that are multiples of a given number. The function should take two parameters: a list of integers and an integer.
"""

def sum_odd_multiples(numbers, num):
    return sum(n for n in numbers if n % 2 == 1 and n % num == 0)