"""
QUESTION:
Write a function `sum_of_odd_numbers(n)` that uses recursion to calculate the sum of all odd numbers from 1 up to `n`. The function should only consider odd numbers in the range and skip even numbers.
"""

def sum_of_odd_numbers(n):
    if n == 1:  
        return 1
    elif n % 2 == 0:  
        return sum_of_odd_numbers(n-1)
    else:  
        return n + sum_of_odd_numbers(n-2)