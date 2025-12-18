"""
QUESTION:
Write a function `nth_element(n)` to calculate the nth element of the Fibonacci sequence, where `n` is a non-negative integer, and the Fibonacci sequence is defined as a series of numbers where a number is the sum of the two preceding ones, starting from 0 and 1.
"""

def nth_element(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return nth_element(n-1) + nth_element(n-2)