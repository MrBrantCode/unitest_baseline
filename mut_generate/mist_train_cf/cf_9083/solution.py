"""
QUESTION:
Write a function `squares_and_sum(n)` that takes a positive integer `n` as input and returns a tuple containing the sum of the squares of the first `n` positive integers and a list of the squares themselves.
"""

def squares_and_sum(n):
    squares = [i**2 for i in range(1, n+1)]
    sum_of_squares = sum(squares)
    return sum_of_squares, squares