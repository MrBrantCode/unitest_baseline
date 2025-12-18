"""
QUESTION:
Implement a function `f` that takes a list of integers `x` as input and returns the sum of the squares of each element in `x` plus the count of even numbers in `x`.
"""

def f(x):
    square_sum = sum([i**2 for i in x])
    even_count = len([i for i in x if i%2 == 0])
    return square_sum + even_count