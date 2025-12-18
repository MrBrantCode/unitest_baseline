"""
QUESTION:
Write a function `sum_numbers(n)` to calculate the sum of integers from 0 to n (inclusive) using recursion, with a time complexity of O(n) and without utilizing any additional data structures or libraries. The function should take an integer n as input and return the calculated sum.
"""

def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n-1)