"""
QUESTION:
Write a function `sum_of_odd_numbers(n)` that uses recursion to calculate the sum of all odd numbers up to `n`. The function should return the total sum of odd numbers.
"""

def sum_of_odd_numbers(n):
    if n == 1:  # base case
        return 1
    elif n % 2 == 0:  # if n is even, skip it
        return sum_of_odd_numbers(n-1)
    else:  # if n is odd, add it to the sum
        return n + sum_of_odd_numbers(n-2)