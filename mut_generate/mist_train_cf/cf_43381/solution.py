"""
QUESTION:
Write a function named `make_positive` that takes a list of integers as an argument and returns a list where all numbers are positive. The solution should be efficient enough to handle a large list of numbers, up to 1,000,000 elements. Do not use any built-in Python functions, including the `abs()` function and unary `-` operator.
"""

def make_positive(num_list):
    def absolute(n):
        mask = n >> 31
        return (n ^ mask) - mask
    return [absolute(num) for num in num_list]